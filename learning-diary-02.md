# Learning Diary #02 (Interactive Data Visualisation)

The second learning diary topic is on "design alternatives, e.g.,
hand-drawn design concepts".

As with the previous week's learning diary, I am using the PPP format
and will detail in each report the following: 1) *Progress* during the
past week, 2) *Plans* for the next week, and 3) *Problems*
encountered, if any.

Project work and this learning diary with live links is available in a
public GitHub repository:
https://github.com/toivotuo/uoh-idv-covid-19/


## Progress

This week's deliverable of design concepts has been implemented in a
Jupyter Notebook. Live version of the notebook is available here:

https://github.com/toivotuo/uoh-idv-covid-19/blob/master/hacking-week-02.ipynb

This week's work has still involved a fair bit of data wrangling. Core
progress items are:

  * The key dataset for the project is the COVID-19 data collected by
    JHU. Last week the data format was analysed, this week work got
    underway in actually prosessing the data into a format that could
    be used as a basis for visualisations. A Python Pandas dataframe
    was used for the data wrangling. See the notebook for the work.

  * For visualisations, experiments on concepts were done with
    Matplotlib and Seaborn. Unfortunately, neither seems to help much
    in creating an actual interactive visualisation. The idea is to
    use for interactivity the Plotly library or alternatively develop
    something more from scratch.

  * As for design concepts, basis line charts where both COVID-19 case
    numbers and financial market performance could be plotted was
    expored. However, this is not really that interesting. The Oxford
    dataset could be used to provide user selectable announcements on
    restrictions imposed by governments. What to ues for this
    technical visualization is an open question. Plotly may offer
    support.

  * Exploring correlations between countries and the different policy
    actions of governments would be interesting. How to visualize
    these is an open question.

Core learnings from the week's work are:

  * Not really a _new_ learning, but always worth remembering that
    data wrangling just does take more time than you expect. I have
    not used Pandas in anything beyond a "Hello, World!"
    before. Getting used to the chosen tooling has thus taken more
    time than expected.

  * It is also hard to think of how to visualize data beyond the usual
    pie charts and bar charts and line charts, etc. But I guess
    providing thinking for some "more interesting" ways to visualize
    data is exactly the point of this course.

## Plans

For the next week, the plan is to finish the data wrangling. There's
some more work to be done to really take the COVID-19 data from JHU to
a format for easy plotting. Now, I've worked on the confirmed cases
data. Also the deaths and recovered data needs to be embedded in the
dataframe.

Then the policy response data from Oxford must be normalised so that
the two dataframes can be sufficiently joined. Finally, market data
needs to be fetched and made ready for using.

## Problems

A problem highlighted as potentially relevant last week is to come up
with visualisations that go beyond the totally ordinary and are at
least a bit interesting. This has been realised. More thinking is
needed for the project to "go beyond line charts".
