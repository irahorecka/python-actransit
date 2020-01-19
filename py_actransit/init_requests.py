# requests support: https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul

import requests
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
import urllib
from api_data import API_Token
from pprint import pprint
BASE_URL = 'https://api.actransit.org/transit'

def get_request(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)
        # sys.exit(1)
    return req


class ACTransit:
    def __init__(self):
        pass
        # '{base}/stops/?token={api_key}'.format(base=BASE_URL, api_key=API_Token)

    def get_gtfs(self, info='all'):
        """
        Returns JSON format of GTFS (General
        Transit Feed Information). Select the
        following kwargs for info: 'all', 'current',
        'download', 'next', {BookingID}
        """
        if not isinstance(info, str):
            info = str(info)
        gtfs_url = '{base}/gtfs/{gtfs_key}/?token={api_key}'.format(
            base=BASE_URL,
            gtfs_key=info.lower(),
            api_key=API_Token)
        gtfs_req = get_request(gtfs_url)

        return gtfs_req.json()


    def get_gtfsrt(self, info='vehicles'):
        """
        Get bus information.
        Return as dict.
        Stable - 2019-01-18
        """
        gtfsrt_url = '{base}/gtfsrt/{gtfs_key}/?token={api_key}'.format(
            base=BASE_URL,
            gtfs_key=info.lower(),
            api_key=API_Token)
        feed = gtfs_realtime_pb2.FeedMessage()

        with urllib.request.urlopen(gtfsrt_url) as response:
            feed.ParseFromString(response.read())
            feed_dict = protobuf_to_dict(feed)
            if info == 'alerts':
                gtfrs_dict = {alert['id']: alert['alert'] for alert in feed_dict['entity']}
            elif info == 'tripupdates':
                gtfrs_dict = {trip['id']: trip['trip_update'] for trip in feed_dict['entity']}
            elif info == 'vehicles':
                gtfrs_dict = {bus['id']: bus['vehicle'] for bus in feed_dict['entity']}

        return gtfrs_dict


    def get_route(self, info=''):
        """
        Return route information for buses.
        :param info:
        :return route_request.json():
        """
        if info != '':
            route_url = '{base}/route/{}/?token={api_key}'.format(
                base=BASE_URL,
                api_key=API_Token)
        route_url = '{base}/routes/?token={api_key}'.format(
            base=BASE_URL,
            api_key=API_Token)
        route_request = get_request(route_url)

        return route_request.json()


if __name__ == '__main__':
    ac = ACTransit()
    x = ac.get_gtfsrt('tripupdates')
    pprint(x)
