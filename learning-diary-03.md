# Learning Diary #03 (Interactive Data Visualisation)

The third learning diary topic is on "exploration on visualization
tools and on prototyping".

As with the previous two week's learning diary, I am using the PPP format
and will detail in each report the following: 1) *Progress* during the
past week, 2) *Plans* for the next week, and 3) *Problems*
encountered, if any.

Project work and this learning diary with live links is available in a
public GitHub repository:
https://github.com/toivotuo/uoh-idv-covid-19/


## Progress

Worked on fetching financial market data for the main stock market
indexes for core set of countries. Yahoo! Finance seems to be the best
free data source. Also Google Finance and IEX Cloud were experimented
with, but Google's public APIs are deprecated and to properly use IEX,
a subscription is needed. Experiments with financial data are saved in
a Jupyter Notebook, see [1].

Earlier, the idea was to use only Jupyter Notebooks with Plotly to
create the interactive application to visualize COVID-19
developments. This might still end up as the final result, but more
likely a simple web app (with Python Django) will be developed that
allows tracking COVID-19 evolution across time and space (i.e.,
comparing different countries). For each time span (selectable day,
week or other period) a set of visualizations are shown using
different data sources. Data sources were investigated and reported on
learning diary #01. See also [2].

Bootstrapped the Django app for a "COVID-19 Visualizer" or
"coviz". For the current code, see [3]. Idea is that the interactive
data visualisation that has been prototyped with Jupyter Notebooks
will be implemented into a deployment version as a Django app.

Idea is to visualise the COVID-19 status via a map with the
possibility to select timeframes and different quantification options
like cases, mortality per capita and so on. Drilling to individual
countries will be possible by clicking the different countries. For
each country then market data correlated with the COVID-19 cases will
be shown.

Experiments with the Python Folium library were done for visualising
the countries and COVID-19 cases. This data is available as a Jupyter
Notebook, see [4].

References:

* [1] https://github.com/toivotuo/uoh-idv-covid-19/blob/master/hacking-week-03-finance.ipynb

* [2] https://github.com/toivotuo/uoh-idv-covid-19/tree/master/data

* [3] https://github.com/toivotuo/uoh-idv-covid-19/tree/master/covid_explorer

* [4] https://github.com/toivotuo/uoh-idv-covid-19/blob/master/hacking-week-03-maps.ipynb


## Plans

Plans were partially covered abobe. In short, the next week plan is to
move the code from Jupyter Notebooks to a Django app and set the
runtime in a Docker container.

A fair bit of work will be needed to make the visualisation usable and
polished. An exiciting week of hacking ahead!


## Problems

No problems really. Fair bit of time has gone into data wrangling with
Pandas and learning the different libraries for visualisation. But
that's been useful, and educational intro into the Python data science
world that I've been ignoring so far.
