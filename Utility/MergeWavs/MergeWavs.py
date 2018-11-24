#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:37:12 2018

@author: schwerbelastung
"""

#################################
### Import required libraries ###
#################################

import scipy.io.wavfile
import argparse
import glob
import numpy as np

#######################
### Parse arguments ###
#######################

parser = argparse.ArgumentParser("Batch")
parser.add_argument("PathToFolder", help="Full path to folder with wav files. Note: End path address with slash /")
args = parser.parse_args()

######################
### Merge function ###
######################

def combineWav(filesToCombine,rate,output):
    mergedFile = []
    for i in range(len(filesToCombine)):
        mergedFile.append(filesToCombine[i])
    mergedFile = np.concatenate(filesToCombine)
    scipy.io.wavfile.write(output,rate,mergedFile)
    
##################
### Load files ###
##################
        
files = []
for filepath in glob.iglob(args.PathToFolder +'*.wav'):
    rate = scipy.io.wavfile.read(filepath)[0] # Read rate from the files
    files.append(filepath)
    
files.sort() # Sort files alphabetically by filename.

filesToMerge = []

for filepath in files:
    filesToMerge.append(scipy.io.wavfile.read(filepath)[1])

#################
### Run batch ###
#################

combineWav(filesToMerge, rate, args.PathToFolder+"Merged.wav") # Combine files
