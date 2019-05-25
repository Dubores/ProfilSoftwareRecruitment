import json
import urllib3


def get_csv_url_from_api():
    http = urllib3.PoolManager()
    urllib3.disable_warnings()
    # get JSON from API
    apidata = http.request('GET', 'https://api.dane.gov.pl/resources/17363').data

    # convert into JSON
    apidata = json.loads(apidata)
    # get URL from JSON
    url = apidata['data']['attributes']['link']
    return url