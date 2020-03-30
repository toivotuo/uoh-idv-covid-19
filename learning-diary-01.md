# Learning Diary #01 (Interactive Data Visualisation)

First learning diary topic is on "project overview, and data
processing (acquisition, cleaning, transformation, annotation, etc)".

For this learning diary, I've selected the PPP format and will detail
in each report the following: 1) *Progress* during the past week, 2)
*Plans* for the next week, and 3) *Problems* encountered, if any.

Project work is available in a public GitHub repository:
https://github.com/toivotuo/uoh-idv-covid-19/

A version of this learning diary with live links is available for
browsing in the GitHub repository linked above.


## Progress

### Core dataset and tooling

For the project data I decided to work on the suggested COVID-19
dataset from Johns Hopkins University (JHU). In order to make the
"data wrangling" and "interactive visualisation" more interested, I
decided to work with also other COVID-19 datasets and try to find
correlations between the data. The interactive visualisation plan is
to allow the data user to explore the correlations.

The plan is to do the data wrangling with Python and implement the
visualisation as a Jupyter Notebook.

### Other datasets investigated

For other data sources, I have investigated and analysed the contents of the
following datasets (links below are to more details on each dataset
investigation):

* [jhu](jhu/): The Johns Hopkins University (JHU) dataset that reports
  COVID-19 cases on a per country basis daily. It would appear that
  this is the "gold standard" public dataset on reported cases and a
  good basis against which the other datasets can be correlated.

* [oxford](oxford/): The Oxford policy responses to COVID-19 dataset
  consists of seven variables per country which provide for an index
  on how stringent the measures to the crisis are in different
  countries. This data will allow looking at correlations between
  policy responses and virus spread as well as economic implications.

* [iif](iif/): The Institute of International Finance (IIF) provides
  two datasets that describe the regulatory and policy responses that
  countries around the world have taken in response to the
  crisis. While the data itself is interesting and appropriate for the
  project, it is unfortunately not immediately usable. The data is
  presented in a human-readable format rather than quantified into a
  format that would be usable in the data visualisation exercise. The
  'iif' dataset is thus not likely used for the project.

* [oecd](oecd/): The Organisation of Economic Cooperation and Development
  (OECD) dataset provides policy response data that is similar to the
  data from the 'oxford' and 'iif' datasets. However, like the 'iif'
  dataset, the OECD data is presented in human-readable format and
  thus not immediately usable for this project.

* [imf](imf/): The International Monetary Fund (IMF) dataset is very
  similar to that from the OECD. Data is human-readable and therefore
  not suitable for this project.

* nytimes: The New York Times provides a quantified dataset for the
  number of cases of COVID-19 on a per county basis in the United
  States. Data is thus similar to the 'jhu' dataset, but with higher
  granularity for the US. The dataset is potentially interesting if
  the interactive visualisation is done both for a global view
  (between countries) and for the US (e.g. between US
  states). Detailed content analysis of the 'nytimes' dataset is not
  yet done.

Based on the above the most relevant datasets for this project are the
'jhu' and 'oxford' datasets. The 'nytimes' may be of interest for a
specific look on the US.

What source to use for market data, is not decided yet. The sources
investigated so far include [IEX Cloud](https://iexcloud.io/) as well
as the data from Google Finance and Yahoo! All of these sources have a
Python library available, see: https://pypi.org/project/iexfinance/
https://pypi.org/project/googlefinance/
https://pypi.org/project/yahoo-finance/ Likely the best source of
these is IEX Cloud that I'll likely use as it may be interesting for
personal projects. Comes with a $9/month cost though.

From the investigated datasets it should be possible to build an
interactive visualisation that explores the correlations between
COVID-19 cases, policy responses and market reactions.


## Plans

For the upcoming week the plan is to work on code that ingests the
datasets and outputs Pandas dataframes. Also routines for calculating
correlations between the datasets is to be done. This should complete
the data wrangling.

Next, initial prototypes for the visualisation are developed, and more
interesting was for visualisation than simply line charts or bar
graphs is looked into. Mostly this work aims to proceed iteratively to
test different visualisations.

A personal motivation for this project is to also understand better
how policy responses affect the virus spread, and how virus spread and
policy responses play out in the markets. Developing interactive
visualisations will hopefully make it easier to spot interesting
avenues for exploring correlations (if not causations).


## Problems

No significant problems in the project have been encountered so far.

It would appear that number of relevant datasets are available, but it
is a bit problematic that most are qualitative, not really
quantitative. While it would be interesting to try and quantify some
of the datasets, this would fall outside of the scope of this
project. Or at the very least, the work would be taking the long way
around before getting to actually visualising the data.

A potential problem for the project is to come up with visualisations
that go beyond the totally ordinary and are at least a bit
interesting.

Also it may turn out that hacking with Python data science tools and
Jupyter Notebook will take more time than expected. While this is
interesting it may be that it doesn't directly contribute to the task
at hand that is the development of an interactive visualisation.
