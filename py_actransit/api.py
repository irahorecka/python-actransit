import requests
import functools
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
import urllib
from api_data import API_Token


class BaseAPI(object):
    BASE_URL = "https://api.actransit.org/transit"
    api = ''
    key = ''
    feed = ''

    def __init__(self, key):
        self.base_url = self.BASE_URL.format(api=self.api)
        self.key = key

    def __repr__(self):
        return "BaseAPI{obj}".format(obj=object)

    def get_protobuf(self, url):
        with urllib.request.urlopen(url) as response:
            self.feed.ParseFromString(response.read())
            feed_dictionary = protobuf_to_dict(self.feed)

            return feed_dictionary

    def get_json(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            raise RuntimeError(error)

        return response.json()



def api_method(method):
    """Decorator for using method signatures to validate and make API calls."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Validate arguments
        method(self, *args, **kwargs)

        url = "{base_url}/{base_api}/{api}?token={key}".format(
            base_url=self.base_url,
            base_api=self.api,
            api=method.__name__,
            key=self.key
        )

        # Generate API response
        if self.feed:
            api_response = self.get_protobuf(url)
        else:
            api_response = self.get_json(url)

        return api_response

    return wrapper



class GTFSRT(BaseAPI):
    api = 'gtfsrt'
    feed = gtfs_realtime_pb2.FeedMessage()

    def __repr__(self):
        return "ACTransit(GTFSRT(api_key))"

    @api_method
    def alerts(self):
        pass

    @api_method
    def tripupdates(self):
        pass

    @api_method
    def vehicles(self):
        pass


class GTFS(BaseAPI):
    api = 'gtfs'

    def __repr__(self):
        return "ACTransit(GTFS(api_key))"

    @api_method
    def all(self):
        pass


class ACTransit(object):
    """Wrapper for the BART API."""
    gtfsrt = None

    def __init__(self, key=API_Token):
        """Initialize the individual APIs with the API key."""
        args = (key,)
        self.gtfsrt = GTFSRT(*args)
        self.gtfs = GTFS(*args)

    def __repr__(self):
        return "ACTransit()"

