import api
from pprint import pprint

if __name__ == '__main__':
    ac = api.ACTransit()
    print(ac.gtfsrt.vehicles())
    print(ac.gtfsrt.alerts())
    print(ac.gtfsrt.tripupdates())

    print(ac.gtfs.all())
    # print(ac.gtfs.current())
    # print(ac.gtfs.download())
    # print(ac.gtfs.next())
