#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:11:47 2018

@author: schwerbelastung
"""

#################################
### Import required libraries ###
#################################

import scipy.io.wavfile
import argparse
import numpy
import glob

####################
### Load + parse ###
####################

parser = argparse.ArgumentParser("Batch")
parser.add_argument("PathToFolder", help="Full path to folder with wav files. Note: End path address with slash /")
parser.add_argument("TargetType", help="Target file type 'csv' (textual csv - slower) or 'npy' (binary numpy - faster)")
parser.add_argument("DownsamplingRate", help="Enter how much you want to downsample. 1 = no downsampling, 2 = 1/2 of samples, n = 1/n of samples")
parser.add_argument("Minutes", help="Enter how many minutes you want to extract from the end of the file")
args = parser.parse_args()

# "/Users/schwerbelastung/Desktop/Junction/DataLocation/IHearVoicesData/Audio/device1_channel1_20181012124210.wav"

####################################
### Define downsampling function ###
####################################

def downsample(pathToWav,targetType,downsamplingRate,minutes):

    file = scipy.io.wavfile.read(pathToWav)
    downsample_rate = int(args.DownsamplingRate)
    mins_to_isolate = int(args.Minutes)
    
    # Get sample rate and file length
    fileLength = len(file[1])
    samplingRate = file[0]
    samplesInMinute = samplingRate*60
#    length_in_seconds = (fileLength / samplingRate)
#    length_in_minutes = length_in_seconds/60

# Extract last n minutes.

    startpoint = fileLength - mins_to_isolate*samplesInMinute    
    sliceObj = slice(startpoint,fileLength)    
    lastpart = file[1][sliceObj]

# Downsample to reduce file size

    downsampled_file = lastpart[::downsample_rate]

# Extract to csv

    if (targetType == 'csv'):
    	numpy.savetxt(pathToWav[:-4]+'_ds'+str(downsample_rate)+'_'+str(mins_to_isolate)+'lastmins.csv', downsampled_file, delimiter=",")
    elif (args.TargetType == 'npy'):
    	numpy.save(pathToWav[:-4]+'_ds'+str(downsample_rate)+'_'+str(mins_to_isolate)+'lastmins.npy', downsampled_file)
    else:
    	parser.print_help()


#################
### Run batch ###
#################
        
files = []
for filepath in glob.iglob(args.PathToFolder +'*.wav'):
    files.append(filepath)

for i in range(len(files)):
    downsample(files[i], args.TargetType, args.DownsamplingRate, args.Minutes)