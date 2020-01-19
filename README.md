# python-ac-transit

A simple <a href="http://www.actransit.org/">Alameda-Contra Costa Transit District</a> API wrapper.
<br>
License: <a href="https://en.wikipedia.org/wiki/MIT_License">MIT License</a>.
<br>

## Installation

```$ pip install python-actransit```

## API

Example usage:
<br>
```
>>> from actransit import ACTransit
>>> ac_transit = ACTransit()
>>> realtime_vehicles = ac_transit.gtfsrt.vehicles()
>>> print(realtime_vehicles)
{'entity': [{'id': '1',
             'vehicle': {'position': {'bearing': 116.0,
                                      'latitude': 37.80388259887695,
                                      'longitude': -122.276611328125,
                                      'speed': 0.0},
                         'timestamp': 1579463770,
                         'trip': {'route_id': '19',
                                  'schedule_relationship': 0,
                                  'trip_id': '751100010'},
                         'vehicle': {'id': '5020'}}},

            #...

            {'id': '237',
             'vehicle': {'position': {'bearing': 141.0,
                                      'latitude': 37.66958999633789,
                                      'longitude': -122.08631134033203,
                                      'speed': 0.0},
                         'timestamp': 1579463765,
                         'trip': {'route_id': '34',
                                  'schedule_relationship': 0,
                                  'trip_id': '685636010'},
                         'vehicle': {'id': '5023'}}}],
 'header': {'gtfs_realtime_version': '1.0',
            'incrementality': 0,
            'timestamp': 1579463788}}
```





