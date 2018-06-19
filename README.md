# Python Client for Localytics Raw Data Export
This is a Python API Client for [Localytics Raw Data Export](https://docs.localytics.com/dev/export-apis.html#log-exports-api). It allows to export all events and sessions captured by Localytics. Data is written in JSON and available on hourly basis as log files.


## Installation

The client is currently best installed installed via Pypi:

    > pip install localytics

## Usage

Let's have a walk through the functionalities through a couple of examples. Start by loading the library.

    > from localytics import Localytics

### Setup and Authentication

In order for you to access the KPI Service, you need to authenticate with `api_key`. Your `api_secret`, once you supply it, will be used throughout the entire session.


#### Using `adjust.setup()` Function

Even if you use the config file, you could still overwrite all settings there in an R session. To do this, you can use
the `adjust.setup()` function or the `set.user.token()`, `set.app.tokens()` functions. See the help pages for each of
those for more details and here is the example:

    > localytics = Localytics(api_key = 'XXXXX', api_secret= 'YYYYY')


### Download Data

There is 1 method that downloads data to local file. Example shows to export data for last 2 days:

    > localytics.download_data(
        app_ids = ['AAAAA', 'BBBBB'],
        start_date = datetime.today() - timedelta(2),
        end_date = datetime.today()
    )

Once you've setup your user token and app tokens, then each of these calls will produce data for you straight away.

You can, more interestingly, also specify parameters. A more complex example:

> localytics.download_data(
    app_ids = ['AAAAA', 'BBBBB'],
    start_date = datetime.today() - timedelta(2),
    end_date = datetime.today(),
    destination_folder = 'data',
    compressed=True
)

On default data are stored in `localytics_data` folder in compressed format `gz`


## Contributions and bug reports.

Contributions and bug reports are only acceptable as GitHub Pull Requests and issues. Thanks!
