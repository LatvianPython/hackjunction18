#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:11:47 2018

@author: schwerbelastung
"""

# Import required libraries

import scipy.io.wavfile

# Load data

file = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Junction/DataLocation/IHearVoicesData/Audio/device1_channel1_20181012124210.wav", mmap=False)

# Calculate data file length
# The 1st array entry has the sampling rate, the 2nd has an array of sound
# values over time.

length_in_seconds = (len(file[1]) / file[0])
length_in_minutes = length_in_seconds/60

print("The audiofile length in seconds: ", length_in_seconds)
print("The audiofile length in minutes: ", length_in_minutes)

# Extract last 1 / 3 / 5 / 10 minutes.
# Logic: Sample rate tells us number of measurements in 1 second, multiply by 60


minute =  file[0]*60
startpoint_1min = len(file[1]) - 1*minute
startpoint_3min = len(file[1]) - 3*minute
startpoint_5min = len(file[1]) - 5*minute
startpoint_10min = len(file[1]) - 10*minute

last_1min_sliceObj = slice(startpoint_1min,len(file[1]))
last_3min_sliceObj = slice(startpoint_3min,len(file[1]))
last_5min_sliceObj = slice(startpoint_5min,len(file[1]))
last_10min_sliceObj = slice(startpoint_10min,len(file[1]))

last_1min = file[1][last_1min_sliceObj]
last_3min = file[1][last_3min_sliceObj]
last_5min = file[1][last_5min_sliceObj]
last_10min = file[1][last_10min_sliceObj]

# Delete unnecessary variables

del (startpoint_1min,startpoint_3min,startpoint_5min,startpoint_10min)

# Downsample to different sizes, to reduce data size

file_downsampled_2 = file[1][::2]
file_downsampled_4 = file[1][::4]
file_downsampled_8 = file[1][::8]
file_downsampled_16 = file[1][::16]
file_downsampled_32 = file[1][::32]


# Extract to csv
