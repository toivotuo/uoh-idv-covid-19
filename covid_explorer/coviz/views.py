#from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    context = {"place": "World"}
#    return render(request, "index.html", context)

def index(request):
    import pandas as pd

    datasource = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(datasource)

    df = df.drop(columns=["Lat", "Long"])  # clean out spatial location columns we don't need
    df = df[df['Province/State'].isna()].drop(columns=['Province/State'])  # FIXME: Cleaning out countries with regional data; removes e.g. Canada and Australia
    df = df.set_index('Country/Region')  # use the country as the index to make transpose work nice
    df = df.transpose()  # transpose rows/columns to give nicely plottable data
    df.index = pd.to_datetime(df.index)  # make the index proper Python 'datetime' for nicer plotting
    df.columns.name = 'Country'  # make the index name nicer

    data = df[['Germany', 'Italy', 'France', 'Spain']]  # select the country subset

    return HttpResponse(data.to_html())
