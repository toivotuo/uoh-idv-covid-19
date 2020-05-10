# PROJECT REPORT

* Course: Interactive Data Visualisation
* Author: Tuomas Toivonen
* Email: tuomas.toivonen@helsinki.fi
* Date: 2020-05-10

## Introduction

This document serves as my project report for the "Interactive Data
Visualisation" course held in the spring semester of 2020 at the
Department of Computer Science, University of Helsinki.

The goal of the project was to develop an interactive data visualisation.

As a topic of the visualisation I chose the current COVID-19
pandemic. A lot of data that is updated on a daily basis is available
on the COVID-19 spread across the world. This makes visualisation of
the pandemic particularly interesting.

As a result of the project work, I have developed a web based
interactive visualisation, the "COVIZ" app, for "COVID-19
Visualizer". The COVIZ app displays COVID-19 data on a world map
(choropleth) and allows filtering the data based on a number of
parameters.

The code for the COVIZ interactive visualisation is available on
GitHub at [1]. An interactive live version of the COVIZ app can be
accessed at [2].

* [1] https://github.com/toivotuo/uoh-idv-covid-19/
* [2] http://www.kasvua.org:8888/coviz/


## Visualisation and data described

As the paradigm for the COVIZ app a choropleth was selected and the
data from ECDC was used.

### Visualisation overview

The core of the COVIZ app is a view that show a world map. The map is
shown as a choropleth.

A choropleth is a type of geographic visualisation that shows chosen
statistical variables with for different geographical areas with
diferent shades. For example, population density comparisons between
countries can be shown with a choropleth where the colours signify
diffent intensities of the population density.

Choroleth was considered as an appropriate core of the COVIZ app as
the idea is to allow the user of the app to compare the diseases
spread across different countries. Thus the choropleth shows
statistical variables on and allows for cross country comparisons. As
the geographic resolution of the choropleth the choice was to use
countries as the basic unit. Rationale for this is that the available
data is aggregated on a per country basis for all countries. For some
countries though, state or province data would be available.

For cross country comparisons the COVIZ app supports a number of
controls that are shown to the right of the choropleth. The supported
controls allow selecting what statistical data is shown on the
choropleth. Supported controls are:

* Date: Allows selecting for which date the data is show. Default is
  to show data for yesterday as we know that the full day's worth of
  data is available.

* Dataset: Allows selecting which of the two core COVID-19 datasets is
  shown, namely, the number of cases or the number of fatalities
  (deaths).

* Relativity: Allows selecting whether absolute numbers are shown or
  whether the choropleth is normalised according to the population of
  each country. If relative data is selected then the data is
  normalised to cases or deaths per million according to the country's
  2018 population.

In addition to the statistical controls, the choropleth shows a marker
for each capital for European countries. Clicking on any of the
markers brings up a popup that shows a bar chart of data for that
country for the past fourteen days. The data shown on the popup is
affected by the same controls that select the statistical variables
shown on the choropleth. The markers and popups allow a user to dive
in deeper and see how the disease situation in each country has
developed over the recent past

The map as implemented in the COVIZ app is dynamic and allows for
scrolling and zooming in and out. A European starting point and zoom
level are selected by default.

### Data sources

The COVIZ app uses a single central data source, namely, the worldwide
COVID-19 cases as delivered by the European Centre for Disease
Prevention and Control (ECDC) [3]. The data is very similar in scope
to the data provided by the Johns Hopkins University (JHU) dataset
[4], but in a format that is easier to process. Indeed, earlier
Jupyter Notebook versions of the COVIZ app used the JHU dataset. The
ECDC dataset was selected as the format is rather easier to use.

Initially, the idea of the app was to also visualise financial data to
show correlations between stock markets, COVID-19 cases and responses
by governments around the world. Practical project considerations,
however, necessitated a more limited approach of focusing on the
COVID-19 epidemiological data only.

Research on other data sources for COVID-19 governmental responses as
well as financial data is documented in the project GitHub repository
[5].

* [3] https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

* [4] https://github.com/CSSEGISandData/COVID-19

* [5] https://github.com/toivotuo/uoh-idv-covid-19/tree/master/data


## Development process and tools

The project was developed in Python and using libraries available in
the Python ecosystem for data wrangling and visualisation.

Development and prototyping were done primarily in Jupyter
Notebooks. The actual COVIZ app was then developed in the Django
framework for Python.

For data processing, the Python Pandas library [6] is used. The ECDC
COVID-19 data is ingested in a Pandas dataframe. The necessary data
munging is done in Pandas as is the filtering based on the controls
that the app user employes.

For the choropleth visualisation, the Python library Folium [7] is
used. Folium is an easy to use, yet flexible library that renders
geographic data with a Pythonic API. Basic maps and related
visualisations are relatively easy to get up and running, and Folium
prototyping in Jupyter works well.

For the bar charts in the per country popups, Vega-Lite [8] is
used. Vega and Vega-Lite are grammars (in JSON) for describing in a
declarative manner interactive graphics. The Folium library supports
rendering graphs described in Vega or Vega-Lite in the popups. The
Python library Altair [9] is used to ingest a filtered Pandas
dataframe and the JSON output in Vega-Lite format is then fed for
Folium to render and display.

* [6] https://pandas.pydata.org/

* [7] https://python-visualization.github.io/folium/

* [8] https://vega.github.io/vega-lite/

* [9] https://altair-viz.github.io/


## Learnings

All in all, this has been a very interesting project - and fun
programming. Building an actual live, interactive visualisation has
also brought into practice the theory of the course. Specific
learnings from the project work outlined below.

As with all programming task, everything usually takes longer than
expected. This has very much been the case with this project. As a
result, the scope of the project was reduced somewhat for the final
deliverable and no financial data visualisation is included in the
final COVIZ app.

Specifically through the project, I have learned a lot about the
Python tooling for creating both static and interactive
visualisations. I've learned to use Pandas dataframes much better than
before, and have realised that effective use of Pandas is a
prerequisite for productive visualisation work in Python. I've also
learned that there are a ton of different libraries available. I'm
happy with the libraries selected for the final product, but would
have liked to use also some of the libraries that were used in working
prototypes in the weekly learning diaries. In addition to the
libraries referred to above, I gained working proficiency with
Matplotlib [10] and Seaborn [11] as well as basic skills with Plotly
[12].

Additionally, through the course, I have (finally!) made Jupyter
Notebooks as a core tool in my Python protoyping toolbox.

* [10] https://matplotlib.org/

* [11] https://seaborn.pydata.org/

* [12] https://plotly.com/python/


## Limitations and future work

The COVIZ app as currently designed and implemented has a number of
limitations that would need to be addressed in any future work. Some
of the limitations are discussed below.

* Performance of the COVIZ app is somewhat limited. The app should be
  considered a visualisation prototype rather than a high volume
  production implementation. For more intensive use, implementation of
  caching facilities would be needed to improve the performance. For
  example, the COVID-19 data is fetched from the ECDC on each load
  rather than cached on the server which adds some additional latency
  to the app use.

* The markers that allow launching popups that show data for specific
  countries are implemented for European countries only. The code
  would support showing markets for all countries with a one line
  change. The reason why only European markers are shown is outlined
  above. Namely, performance. As the data shown with the popups is
  currently pre-rendered, showing popups for all countries of the
  world reduces usability.

* More skills in frontend development and Javascript would have
  allowed me to make the visualisation more performant as well as the
  interactivity more streamlined and fluid. In the current
  implementation the visualisation flow is based on HTTP
  request-response loop reloading the whole page. This makes the app
  less pleasant to use and data exlporation slower.


## Conclusion

This project work has resulted in a simple web app, COVIZ, the "COVID
Visualizer", for COVID-19 epidemiological data visualisation. The app
is relatively simple in function, but also simple for a user to just
start using without special instructions. The project has been
implemented with standard Python libraries and is thus easily
extensible. Using the app, a user gains better understanding of the
spread of the COVID-19 disease around the world.
