# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:24:38 2022
@author: norm

Calculate the distance from Earth to Saturn.
Uses the Skyfield package and the Jet Propulsion Laboratory's DE440
ephemeris to calculate the planets' distance from Earth at a specific point in
the future. The calculations are dumped to `stdout` as a CSV file.
"""

import csv
import datetime
import sys

from skyfield.api import load

output = csv.writer(sys.stdout)
output.writerow(("planet", "date", "distance"))

# de440.bsp covers the years 1550 to 2650
planets = load("de440.bsp")
earth, saturn = (
    planets["EARTH"],
    planets["SATURN BARYCENTER"],
)

ts = load.timescale()

# Use the date Bob starts his journey
date = datetime.date(2133, 8, 17)

# This will calculate the distance to Saturn over the 6 days of Bob's trip.
# Really, only the last day is probably most relevant in terms of the distance.
while date != datetime.date(2133, 8, 23):
    t = ts.utc(date)
    earth_at_time = earth.at(t)
    astrometric = earth_at_time.observe(saturn)
    _, _, distance = astrometric.radec()
    output.writerow(
        ('Saturn', t.utc_strftime("%Y-%m-%d"), distance.au)
    )
    date += datetime.timedelta(days = 1)
