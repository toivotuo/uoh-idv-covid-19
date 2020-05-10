from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "date": "2020-05-01",
    }

    return render(request, "index.html", context)


def controls(request):
    """
    A little view to provide controls in an iframe for the choropleth
    iframe. Hack to avoid using any JS in the app.
    """
    context = {
        "date": "2020-05-01",
    }

    resp = render(request, "controls.html", context)
    resp['X-Frame-Options'] = 'SAMEORIGIN'  # Let the controls render in an <iframe>
    return resp


def map(request, date, dataset):
    """
    Render a choropleth of COVID-19 cases using the data from the ECDC.
    """
    import pandas as pd
    import datetime
    import folium

    # Fetch and setup the data from ECDC.

    # FIXME: We have a naive setup here that fetches the data form the
    # ECDC with every request. Caching the data would be much better.

    # url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/"
    url = "/tmp/ecdc.csv"  # FIXME: Fails on deployment

    data = pd.read_csv(url)

    data = data[data['dateRep'] == date.strftime("%d/%m/%Y")]

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
        legend_name="COVID-19 {} on {} (Data source: ECDC)".format(dataset, date.strftime('%Y-%m-%d')),
    ).add_to(map)

    resp = HttpResponse(map.get_root().render())
    resp['X-Frame-Options'] = 'SAMEORIGIN'  # Let the map render in an <iframe>
    return resp


def map_old(request):
    """Render a choropleth (coloured map) of COVID-19 cases. Uses data from JHU."""
    import pandas as pd
    import folium
    import pycountry
    import json
    import requests

    # FIXME: Remove this method that was done with the hard to wrangle JHU data.

    # First, fetch and wrangle the relevant data.

    country_geo = '/tmp/world-countries.json'

    # FIXME: Not an efficient approach to read the latest data
    # directly from GitHub on every request.

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
