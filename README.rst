Python Client for Localytics Raw Data Export
==============================================
This is a Python API Client for [Localytics Raw Data Export](https://docs.localytics.com/dev/export-apis.html#log-exports-api). It allows to export all events and sessions captured by Localytics. Data is written in JSON and available on hourly basis as log files.


Installation
----------------------
The client is currently best installed via Pypi:
.. code-block:: bash
    $ pip install localytics

Usage
---------------------
Let's have a walk through the functionalities through a couple of examples. Start by loading the library.

.. code-block:: python
    >>> from localytics import Localytics

*Setup and Authentication*
In order for you to access the KPI Service, you need to authenticate with `api_key`. Your `api_secret`, once you supply it, will be used throughout the entire session.

.. code-block:: python
    >>> localytics = Localytics(api_key = 'XXXXX', api_secret= 'YYYYY')


*Download Data*
There is 1 method that downloads data to local file. Example shows to export data for last 2 days:
.. code-block:: python
    >>> localytics.download_data(
            app_ids = ['AAAAA', 'BBBBB'],
            start_date = datetime.today() - timedelta(2),
            end_date = datetime.today()
        )

Once you've setup your user token and app tokens, then each of these calls will produce data for you straight away.

You can, more interestingly, also specify parameters. A more complex example:
.. code-block:: python
    >>> localytics.download_data(
        app_ids = ['AAAAA', 'BBBBB'],
        start_date = datetime.today() - timedelta(2),
        end_date = datetime.today(),
        destination_folder = 'data',
        compressed=True
    )

On default data are stored in `localytics_data` folder, compressed in `gz` format.


Contributions and bug reports
------------------------------
Contributions and bug reports are only acceptable as GitHub Pull Requests and issues. Thanks!
