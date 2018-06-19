import requests
from datetime import timedelta, datetime
from progressbar import ProgressBar
import time
import os
import shutil
import gzip

class Localytics():

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    @staticmethod
    def get_endpoints(app_ids, start_date, end_date):
        """
        Get URLs for data you want to download
        """
        base_url = 'https://api.localytics.com/v1/exports/analytics/logs/'
        start_date_casted = start_date.replace(microsecond=0,second=0,minute=0)
        end_date_casted = end_date.replace(microsecond=0,second=0,minute=0)
        delta = end_date_casted - start_date_casted
        dates_to_download = [start_date_casted + timedelta(hours=i) for i in range(delta.days * 24 + 1)]
        date_urls = [str(i.year) + '/' + str(i.month) + '/' + str(i.day) + '/' + str(i.hour) for i in dates_to_download]
        urls = [base_url + app + '/' + str(date) for date in date_urls for app in app_ids]
        return urls

    @staticmethod
    def save_file(response, filename, destination_folder, compressed):
        with open(destination_folder + '/' + filename, 'wb') as new_file:
                new_file.write(response.content)
        if compressed == False:
            with gzip.open(destination_folder + '/' + filename, 'rb') as f_in:
                with open(destination_folder + '/' + filename[:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    os.remove(destination_folder + '/' + filename)

    def download_data(self, app_ids, start_date, end_date, destination_folder='localytics_data', compressed=True):
        """
        Download data from localytics
        """
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
        os.makedirs(destination_folder)

        endpoints = self.get_endpoints(app_ids, start_date, end_date)
        session = requests.Session()
        session.auth = (self.api_key, self.api_secret)

        pbar = ProgressBar()
        for endpoint in pbar(endpoints):
            filename = endpoint.split('/')[7][:10] + '__' + '_'.join(endpoint.split('/')[8:]) + '.log.gz'
            presigned_url = session.get(endpoint, stream=True).url
            response = requests.get(presigned_url, stream=True)
            self.save_file(response, filename, destination_folder, compressed=compressed)

        return print('Data downloaded!')
