#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:42:38 2022
@author: norm
"""

# imports
import numpy as np

# constants
c = 299792458
g = 9.80665
year = 31556952

c_ly = 1.0
ly = c * year
g_ly = g * pow(year, 2) / ly

# variables
distance = 16.3
ship_acceleration = 1.0 * g_ly

# functions
def earthTimeToStarSystem(d, a):
    return np.sqrt(pow(d / c_ly, 2) + 2.0 * d / a)

def shipTimeToStarSystem(d, a):
    return 2.0 * c_ly / a * np.arccosh(a * d / (2.0 * pow(c_ly, 2)) + 1)

def speedAtMidpoint(t, a):
    return a * t / np.sqrt(1.0 + pow(a * t / c_ly, 2))

earth_time = round(2.0 * earthTimeToStarSystem(distance / 2.0, ship_acceleration), 6)
ships_time = round(shipTimeToStarSystem(distance, ship_acceleration), 6)
speed_at_midpoint = round(speedAtMidpoint(earth_time / 2, ship_acceleration), 6)
print("Earth time:", earth_time, "years")
print("Ship's time:", ships_time, "years")
print("Speed at midpoint:", speed_at_midpoint, "fraction of c")
