import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from .helpers import make_marker

class ControlsForm(forms.Form):
    date = forms.DateField(
        label="Date",
        help_text="Show data for this date",
    )
    dataset = forms.ChoiceField(
        label="Dataset",
        choices=(
            ('cases', 'Cases'),
            ('deaths', 'Deaths'),
        ),
        help_text="Show diagnosed cases or fatalities",
    )
    relativity = forms.ChoiceField(
        label="Relativity",
        choices=(
            ('absolute', 'Absolute'),
            ('relative', 'Relative'),
        ),
        help_text="Show numbers as absolute or relative to million inhabitants",
    )


def index(request):
    """
    Here be dragons (and COVID-19 maps).
    """
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    defaults = {
        "date": yesterday.strftime("%Y-%m-%d"),
        "dataset": "cases",
        "relativity": "absolute",
    }

    if request.method == "POST":
        form = ControlsForm(request.POST)
        if form.is_valid():
            pass  # do nothing
    else:
        form = ControlsForm(initial=defaults)

    context = {
        "form": form,
    }

    return render(request, "index.html", context)


def map(request, date, dataset, relativity):
    """
    Render a choropleth of COVID-19 cases using the data from the ECDC.

    :data: Show data for specific date
    :dataset: Show 'cases' or 'deaths'
    :relativity: Show 'absolute' or 'relative' case numbers
    """
    import pandas as pd
    import datetime
    import folium

    # Fetch and setup the data from ECDC.

    # FIXME: We have a naive setup here that fetches the data form the
    # ECDC with every request. Caching the data would be much better.

    # url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/"
    url = "/tmp/ecdc.csv"  # FIXME: Fails on deployment

    raw_data = pd.read_csv(url)
    data = raw_data  # FIXME: hack

    data = data[data['dateRep'] == date.strftime("%d/%m/%Y")]

    # By default, we assume absolute numbers and do no number
    # crunching. If relative (per 1m population) is requested, then we
    # calculate the relative load and do binning to avoid off the
    # charts numbers for small countries.

    if relativity == 'relative':
        data[dataset] = data[dataset] / (data['popData2018'] / 1000000)  # per million
        bins = data[dataset].quantile([0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1.0])
    else:
        pass

    # Render the data on a choropleth.

    country_geo = "/tmp/world-countries.json" # FIXME: Fails on deployment

    map = folium.Map(
        location=[45,0],
        zoom_start=3.0,
    )

    folium.Choropleth(
        geo_data=country_geo,
        data=data,
        columns=['countryterritoryCode', dataset],
        key_on='feature.id',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        bins=9,
        legend_name="COVID-19 {} {} on {} (Data source: ECDC)".format(relativity, dataset, date.strftime('%Y-%m-%d')),
    ).add_to(map)

    # Add a marker for each country to the map.

    # Source for capitals data: https://www.kaggle.com/nikitagrec/world-capitals-gps

    caps = pd.read_csv("/tmp/capitals.csv")  # FIXME: deployment issue
    caps = caps[caps['ContinentName'] == 'Europe']

    def rebase_date(date):
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        return date

    raw_data.dateRep = raw_data.dateRep.apply(rebase_date)
    raw_data.sort_values(by=['dateRep'], inplace=True)
    before_date = datetime.datetime(date.year, date.month, date.day)
    raw_data = raw_data[raw_data['dateRep'] <= before_date]

    for index, row in caps[0:250].iterrows():
        country = row['CountryCode']
        lat = row['CapitalLatitude']
        lon = row['CapitalLongitude']

        df = raw_data[raw_data['geoId'] == country]
        df = df.tail(14)

        if relativity == 'relative':
            df[dataset] = df[dataset] / (df['popData2018'] / 1000000)  # per million

        marker = make_marker(
            df, country, lat, lon, dataset,
        )
        marker.add_to(map)

    # Return the HTTP response.

    resp = HttpResponse(map.get_root().render())
    resp['X-Frame-Options'] = 'SAMEORIGIN'  # Let the map render in an <iframe>
    return resp
