#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:11:47 2018

@author: schwerbelastung
"""

# Import required libraries

import scipy.io.wavfile
import argparse
import numpy

# Load data

# "/Users/schwerbelastung/Desktop/Junction/DataLocation/IHearVoicesData/Audio/device1_channel1_20181012124210.wav"

parser = argparse.ArgumentParser("Downsample")
parser.add_argument("PathToWav", help="Full path to WAV file, CSV will be output as 'csv' or 'npy' with the same name")
parser.add_argument("TargetType", help="Target file type 'csv' (textual csv - slower) or 'npy' (binary numpy - faster)")
parser.add_argument("DownsamplingRate", help="Enter how much you want to downsample. 1 = no downsampling, 2 = 1/2 of samples, n = 1/n of samples")
parser.add_argument("Minutes", help="Enter how much you want to downsample. 1 = no downsampling, 2 = 1/2 of samples, n = 1/n of samples.")
args = parser.parse_args()

file = scipy.io.wavfile.read(args.PathToWav)
downsample_rate = int(args.DownsamplingRate)
mins_to_isolate = int(args.Minutes)




# Get sample rate
fileLength = len(file[1])
samplingRate = file[0]
samplesInMinute = samplingRate*60

# Calculate data file length
# The 1st array entry has the sampling rate, the 2nd has an array of sound
# values over time.

length_in_seconds = (fileLength / samplingRate)
length_in_minutes = length_in_seconds/60

print("The audiofile length in seconds: ", length_in_seconds)
print("The audiofile length in minutes: ", length_in_minutes)

# Extract last n minutes.

startpoint = fileLength - mins_to_isolate

sliceObj = slice(startpoint,fileLength)

lastpart = file[1][sliceObj]

# Downsample to reduce file size

downsampled_file = file[1][::downsample_rate]


# Extract to csv

if (args.TargetType == 'csv'):
	numpy.savetxt(args.PathToWav+'.csv', downsampled_file, delimiter=",")
elif (args.TargetType == 'npy'):
	numpy.save(args.PathToWav+'.npy', downsampled_file)
else:
	parser.print_help()
