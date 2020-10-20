# GPS_TO_KML
Methods to generate KMLs based on GPS data input
October 2020

This document contains information specific to operating the GPS Tracker and 
viewing in Google Earth.

Setup:
1. Extract files to same directory.
2. Open GPSTracker.py to set up file pathways.
3. Will need to set pathway for IDdict.json (Line 9) and for tracker.kml (Line 38).
4. Copy test script for browser to clipboard (Line 37)
5. Save and run GPSTracker.py - Should return "Starting server..." and "Server is running!"
6. Open browser (see notes below) and enter the test script.
7. Open Google Earth and add in a Network Link (Add -> Network Link).
8. Set the file pathway for tracker.kml
9. Set Refresh to Time-Based Periodically and 5 secs
10. Make a change to the browser script name, latitude, longitude, or altitude and enter.
11. Observe the placemark change in Google Earth after 5 seconds.

Notes:
Tested using Chrome and Firefox.
GPSTracker can handle multiple entries simultaneously
