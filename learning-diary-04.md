# Learning Diary #04 (Interactive Data Visualisation)

The third learning diary topic is on "iterations, and final design
decision".

As with the previous two week's learning diary, I am using the PPP format
and will detail in each report the following: 1) *Progress* during the
past week, 2) *Plans* for the next week, and 3) *Problems*
encountered, if any.

Project work and this learning diary with live links is available in a
public GitHub repository:
https://github.com/toivotuo/uoh-idv-covid-19/


## Progress

This week the project hacking has continued with working on Jupyter
Notebooks for prototyping and then converting the results over to the
actual COVID-19 visualization app implemented with Python Django.

Several interesting developments with data and tools were made during
the work in the past week:

  * There's COVID-19 data drom the ECDC (European Centre for Disease
    Control) that is easier to work with than the JHU COVID-19
    data. Less data conversions are needed. Code has not yet been
    converted from the JHU to ECDC data, but for the final version
    this is the plan for more maintainable code.

  * Work with Folium visualizations continued. A facility was found in
    Folium that allows rendering markers (for example, dropped pins)
    on the map that provide for popups that render HTML. This allows
    making the maps immediately interactive and a gateway to per
    country data.

  * It was also found out that Folium can render in popups data that
    is input in the VEGA-Lite [1] format. This, in combination with
    HTML rendering, will allow the core COVID-19 data to be
    immediately rendered on a per country basis. Should provide the
    needed interactivity.

  * For VEGA-Lite generation (instead of crunching that manually), the
    Altair [2] Python library is something that is planned to be used in
    the final project submission.

  * Also a bit of investigation was done one the Bokeh [3] library that
    might be a nice tool to give a little bit more interactivity still
    to the results.

The toolset is now decided and there should not be a need to wrangle
tools or data (too much) anymore.

Results of this week's work are at [4] and [5]. The notebook in [4] is
developed further from last week's notebook (but reused).

References:

* [1] https://github.com/vega/vega-lite
* [2] https://github.com/altair-viz/altair
* [3] https://docs.bokeh.org/en/latest/index.html
* [4] https://github.com/toivotuo/uoh-idv-covid-19/blob/master/hacking-week-03-maps.ipynb
* [5] https://github.com/toivotuo/uoh-idv-covid-19/tree/master/covid_explorer


## Plans

In terms of final design decisions, the roadmap to the final product
is now clear. A Python Django based web app is delivered. The primary
paradigm is presenting a map where different COVID-19 visualizations
can be selected as chorolopeths. Each of the country is
clickable. When a country is clicked, a popup with more detailed data
on that country will be brought up.

Finally, in the delivered visualization, an expanded per country view
can be opened up from the map where a single page will show all the
data that is available on COVID-19 and that specific country.


## Problems

No problems expected. Lots of hacking needed over the May Day long
weekend!

I had wished to finish more of the final deliverable during this week,
but turns out that it was a more learning week with the final
deliverable still needing a fair bit of coding.
