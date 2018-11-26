#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:34:05 2018

@author: schwerbelastung
"""

#################################
### Import required libraries ###
#################################

import scipy.io.wavfile
import argparse
import os

#######################
### Parse arguments ###
#######################

parser = argparse.ArgumentParser("Batch")
parser.add_argument("WorkFolder", help="Folder for input and output file. End with slash /")
parser.add_argument("InputFileName", help="Input file name")
parser.add_argument("OutputFileName", help = "Output file name")
parser.add_argument("StartMinute", help="Starting minute (e.g., 5 in 5:11)")
parser.add_argument("StartSecond", help="Starting second (e.g., 11 in 5:11)")
parser.add_argument("EndMinute", help="Ending minute (e.g., 8 in 8:42)")
parser.add_argument("EndSecond", help="Ending second (e.g., 42 in 8:42)")
args = parser.parse_args()

os.chdir(args.WorkFolder)


#####################
### Snip function ###
#####################

fileToSnip = scipy.io.wavfile.read(args.InputFileName)
samplingRate = fileToSnip[0]

startInTimeUnits = (int(args.StartMinute)*60 + int(args.StartSecond)) * samplingRate
endInTimeUnits = (int(args.EndMinute)*60 + int(args.EndSecond)) * samplingRate

newFile = fileToSnip[1][int(startInTimeUnits):int((endInTimeUnits+1))]

scipy.io.wavfile.write(args.OutputFileName,samplingRate,newFile)


##############
### Run it ###
##############

#runfile('/Users/schwerbelastung/Dropbox/1 Uni/Junction/hackjunction18/Utility/Spectogram/Snippingtool/snip.py', 
#        wdir='/Users/schwerbelastung/Dropbox/1 Uni/Junction/hackjunction18/Utility/Spectogram/Snippingtool',
#        args = '/Users/schwerbelastung/Desktop/Incidents/wat/ Incident_1_start_201810211715.wav output.wav 2 10 3 15')