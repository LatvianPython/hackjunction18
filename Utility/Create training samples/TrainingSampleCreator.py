#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 08:03:18 2018

@author: schwerbelastung
"""

# This script creates short training samples out of a long audio file for
# machine learning algorithms.


#################################
### Import required libraries ###
#################################

import scipy.io.wavfile
import argparse
import os

####################
### Load + parse ###
####################

parser = argparse.ArgumentParser("Batch")
parser.add_argument("Folder", help="Working folder: The location of source and output files")
parser.add_argument("Wavfile", help="Filename of the source wav file.")
parser.add_argument("TargetLength", help="Training sample length in seconds")
parser.add_argument("Overlap", help="Do you want the samples to have overlapping data? If set to 0, all samples have only unique data.")
args = parser.parse_args()

os.chdir(args.Folder)

###############################
### Training sample creator ###
###############################

sourceFile = scipy.io.wavfile.read(args.Wavfile)
samplingRate = sourceFile[0] # Sample rate is stored here

fileLengthInFullSeconds = int(len(sourceFile[1])/samplingRate) # File length = number of samples / sample rate

numberOfUniquePossibilities = int(fileLengthInFullSeconds/int(args.TargetLength)) # Cast to int to round down

numberOfOverlappingPossibilities = fileLengthInFullSeconds - int(args.TargetLength) + 1

if(args.Overlap == "1"):
    startingTimePoints = list(range(0,numberOfOverlappingPossibilities))
elif(args.Overlap == "0"):
    startingTimePoints = [i * int(args.TargetLength) for i in list(range(0,numberOfUniquePossibilities))]

for i in range(len(startingTimePoints)):
    startingPoint = startingTimePoints[i]*samplingRate
    endPoint = startingPoint + int(args.TargetLength)*samplingRate
    trainingSample = sourceFile[1][startingPoint:endPoint]
    destinationFile = scipy.io.wavfile.write("TrainingSample_" + str(i + 1), samplingRate, trainingSample )