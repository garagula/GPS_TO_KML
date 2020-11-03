# GPS_TO_KML - October 2020
Methods to generate KMLs based on GPS data input

This document contains information specific to operating the GPS Tracker and 
viewing in Google Earth.

Setup:
1. Extract files to same directory.
2. Optional: Set filepath in GPSTracker.py for IDdict.json (Line 9) and for tracker.kml (Line 38).

* Default location for files is script project folder.

3. Save and run GPSTracker.py - Terminal should echo "Starting server..." and "Server is running!"

* With terminal pointed to project folder with the script:

'''python GPSTracker.py'''

4. Open browser, and enter HTTP Request to test server.

```http://localhost:9000/id=111&lat=30&lon=-95&alt=0```

5. Open Google Earth and add in a Network Link (Add -> Network Link).
6. Set the file pathway for tracker.kml.
7. Set Refresh to Time-Based Periodically and 5 secs.
8. Make a change to the browser HTTP request name, latitude, longitude, or altitude and enter.
9. Observe the placemark change in Google Earth after 5 seconds.

Notes:
Tested using Chrome and Firefox.
GPSTracker can handle multiple entries simultaneously
