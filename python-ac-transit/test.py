import api
from pprint import pprint

if __name__ == '__main__':
    ac = api.ACTransit()
    pprint(ac.gtfsrt.vehicles())
    pprint(ac.gtfsrt.alerts())
    pprint(ac.gtfsrt.tripupdates())

    pprint(ac.gtfs.all())
    # print(ac.gtfs.current())
    # print(ac.gtfs.download())
    # print(ac.gtfs.next())
