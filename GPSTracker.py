#!/usr/bin/env python

import json
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer
from textwrap import dedent

#path to json library with device ID and friendly name
with open("IDdict.json") as f:
    ID2NAME = json.load(f)

class OsmAndHandler(BaseHTTPRequestHandler):
    def __init__(self, devices, *args):
        self.devices = devices
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        if not self.path.startswith("/id"):
            return

        data = urllib.parse.parse_qs(self.path)
        device_ip = self.client_address[0]
        device_id = (
            ID2NAME.get(data.get("/id", [None])[0]) or data.get("/id", [device_ip])[0]
        )
        device = {
            device_id: {
                "lat": data["lat"][0],  #latitude
                "lon": data["lon"][0],  #longitude
                "alt": data["alt"][0],  #altitude
                            }
        }
        self.devices.update(device)

        # Updated location, now write KML with ALL objects
        # Test script for browser: http://localhost:9000/id=111&lat=30&lon=-95&alt=0
        with open("tracker.kml", "w") as f:
            header = """\
            <?xml version="1.0" encoding="UTF-8"?>
            <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:kml="http://www.opengis.net/kml/2.2">
            <Document>
                <Folder>
                    <name>GPS Tracker</name>
            """
            entry = """\
                    <Placemark>
                        <name>{device}</name>
                        <Point>
                            <coordinates>{lon},{lat},{alt}</coordinates>
                            <altitudeMode>relativeToGround</altitudeMode>
                        </Point>
                    </Placemark>
            """
            footer = """\
                </Folder>
            </Document>
            </kml>
            """

            f.write(dedent(header))
            for device in self.devices:
                lat = self.devices[device]["lat"]
                lon = self.devices[device]["lon"]
                alt = self.devices[device]["alt"]
                lines = dedent(
                    (entry.format(device=device, lat=lat, lon=lon, alt=alt))
                ).splitlines()
                for line in lines:
                    f.write(f"{' ' * 8}{line}\n")
            f.write(dedent(footer))

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Send message back to client
        message = "Location received!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

def osmand2kml_server(devices):
    def handler(*args):
        OsmAndHandler(devices, *args)

    server = HTTPServer(("localhost", 9000), handler)
    print("Server is running!")
    server.serve_forever()

def main():
    devices = {}
    osmand2kml_server(devices)

if __name__ == "__main__":
    print("Starting server...")
    main()
    