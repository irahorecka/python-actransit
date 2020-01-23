"""
Unit testing for actransit module in ../actransit
"""

import os
from pathlib import Path
import sys
import unittest
os.chdir(Path(__file__).parent)
os.chdir('../actransit')
sys.path.append(os.getcwd())  # required for relative file fetching - run in 'test' directory

from actransit import ACTransit
ac_transit = ACTransit()


class TestACTransit(unittest.TestCase):

    def test_gfts_all(self):
        result = ac_transit.gtfs.all()
        self.assertIsInstance(result, list)

    def test_gtfsrt_vehicles(self):
        result = ac_transit.gtfsrt.vehicles()
        self.assertIsInstance(result, dict)

    def test_gtfsrt_alerts(self):
        result = ac_transit.gtfsrt.alerts()
        self.assertIsInstance(result, dict)

    def test_gtfsrt_tripupdates(self):
        result = ac_transit.gtfsrt.tripupdates()
        self.assertIsInstance(result, dict)

    def test_route_all(self):
        result = ac_transit.route.all()
        self.assertIsInstance(result, list)

    def test_route_directions(self):
        # must have kwarg rt
        # must add valid route number of HTTPError will result
        result = ac_transit.route.directions(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.directions(rt='212')
        self.assertIsInstance(result, dict)

    def test_route_trips(self):
        # must have kwarg rt
        result = ac_transit.route.trips(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.trips(rt='212')
        self.assertIsInstance(result, dict)

    def test_route_tripsestimates(self):
        # must have kwarg rt
        result = ac_transit.route.tripsestimates(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.tripsestimates(rt=212, fromStopId=51103, toStopId=53305)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.tripsestimates(rt='212', fromStopId='51103', toStopId='53305')
        self.assertIsInstance(result, dict)

    def test_route_tripsinstructions(self):
        # must have kwarg rt
        result = ac_transit.route.tripsinstructions(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.tripsinstructions(rt=212, direction='NORTH')
        self.assertIsInstance(result, dict)

    def test_route_vehicles(self):
        # must have kwarg rt
        result = ac_transit.route.vehicles(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.route.vehicles(rt='212')
        self.assertIsInstance(result, dict)

    def test_actrealtime_detour(self):
        result = ac_transit.actrealtime.detour()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.detour(rt=212)
        self.assertIsInstance(result, dict)
        # rtdir results in invalid call
        result = ac_transit.actrealtime.detour(rt=212, rtdir='Northbound')
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.detour(212)
        self.assertIsInstance(result, dict)
        # invalid call
        result = ac_transit.actrealtime.detour(212, 'Northbound')
        self.assertIsInstance(result, dict)
        # invalid call
        result = ac_transit.actrealtime.detour('NORTH', 212)
        self.assertIsInstance(result, dict)

    def test_actrealtime_direction(self):
        # must have rt kwarg
        result = ac_transit.actrealtime.direction(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.direction(rt='212')
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.direction(212)
        self.assertIsInstance(result, dict)

    def test_actrealtime_line(self):
        # no kwargs
        result = ac_transit.actrealtime.line()
        self.assertIsInstance(result, dict)

    def test_actrealtime_locale(self):
        # no kwargs
        result = ac_transit.actrealtime.locale()
        self.assertIsInstance(result, dict)

    def test_actrealtime_pattern(self):
        result = ac_transit.actrealtime.pattern()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.pattern(rt=212)
        self.assertIsInstance(result, dict)
        # pid + rt together results in invalid call
        result = ac_transit.actrealtime.pattern(pid=212, rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.pattern(212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.pattern(212, 212)
        self.assertIsInstance(result, dict)

    def test_actrealtime_prediction(self):
        # if invalid request, invalid JSON returns
        result = ac_transit.actrealtime.prediction()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.prediction(stpid=51333)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.prediction(stpid=51333, rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.prediction(stpid=51333, rt=212, top=10)
        self.assertIsInstance(result, dict)

    def test_actrealtime_time(self):
        result = ac_transit.actrealtime.time()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.time(unixTime=1579715850)
        self.assertIsInstance(result, dict)

    def test_actrealtime_servicebulletin(self):
        result = ac_transit.actrealtime.servicebulletin()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.servicebulletin(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.servicebulletin(rt=212, rtdir='NORTH')
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.servicebulletin(rt=212, rtdir='NORTH', stpid=51333)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.servicebulletin(rt=212, stpid=51333)
        self.assertIsInstance(result, dict)

    def test_actrealtime_stop(self):
        result = ac_transit.actrealtime.stop()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.stop(rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.stop(rt=212, dir='NORTH')
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.stop(rt=212, dir='NORTH', stpid=51333)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.stop(rt=212, stpid=51333)
        self.assertIsInstance(result, dict)

    def test_actrealtime_vehicle(self):
        result = ac_transit.actrealtime.vehicle()
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.vehicle(vid=1341)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.vehicle(vid=1341, rt=212)
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.vehicle(rt=212, vid='1341')
        self.assertIsInstance(result, dict)
        result = ac_transit.actrealtime.vehicle(1341)
        self.assertIsInstance(result, dict)

    def test_vehicle_id(self):
        # must have kwarg id
        result = ac_transit.vehicle.id(id=1341)
        self.assertIsInstance(result, dict)
        result = ac_transit.vehicle.id(1341)
        self.assertIsInstance(result, dict)

    def test_stops_all(self):
        # no kwargs
        result = ac_transit.stops.all()
        self.assertIsInstance(result, list)

    def test_stops_predictions(self):
        # must have kwarg stpid
        result = ac_transit.stops.predictions(stpid=51333)
        self.assertIsInstance(result, list)
        result = ac_transit.stops.predictions(51333)
        self.assertIsInstance(result, list)

    def test_stops_routes(self):
        # must have kwarg stpid
        result = ac_transit.stops.routes(stpid=51333)
        self.assertIsInstance(result, list)
        result = ac_transit.stops.predictions(51333)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
