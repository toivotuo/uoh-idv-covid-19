#from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    context = {"place": "World"}
#    return render(request, "index.html", context)

def index(request):
    """ Dummy index page to have something actually loading. """
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


def map(request):
    """Render a choropleth (coloured map) of COVID-19 cases."""
    import pandas as pd
    import folium
    import pycountry
    import json
    import requests

    # FIXME: Using rather the ECDC data would be better. Less
    # wrangling needed than with the JHU data.

    # First, fetch and wrangle the relevant data.

    country_geo = '/tmp/world-countries.json'

    # FIXME: Dumb to read the latest data directly from GitHub on
    # every request.

    datasource = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    data = pd.read_csv(datasource)

    data = data.drop(columns=["Lat", "Long"])  # clean out spatial location columns we don't need
    # FIXME: Cleaning out countries with regional data; removes e.g. Canada and Australia
    data = data[data['Province/State'].isna()].drop(columns=['Province/State'])

    data = data.rename(columns={"Country/Region": "Country"})

    # Convert the country names
    def rebase(country_name):
        country = pycountry.countries.get(name=country_name)
        if not country:
            return 'N/A'  # FIXME
        return country.alpha_3

    data.Country = data.Country.apply(rebase)

    # Second, generate and render the map.

    map = folium.Map(
        location=[45, 0],
        zoom_start=3,
    )

    date = "4/26/20"  # FIXME: Make data selection dynamic in the web app.

    folium.Choropleth(
        geo_data=country_geo,
        data=data,
        columns=['Country', date],
        key_on='feature.id',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Cases of COVID-19",
    ).add_to(map)

    # Third, let's set some markers on the map.

    # FIXME: We should have each country's data as markers (or
    # preferably making each country clickable).

    folium.Marker(
        location=[51.50, 0],
        popup='<b>Greenwich</b>',
        icon=folium.Icon(icon='cloud')
    ).add_to(map)

    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    dataviz = json.loads(requests.get(f'{url}/vis2.json').text)

    folium.Marker(
        location=[60.17, 24.94],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(dataviz, width=450, height=250))
    ).add_to(map)

    # FIXME: The map should be rendered in an iframe.

    return HttpResponse(map.get_root().render())
