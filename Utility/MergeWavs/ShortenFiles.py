#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:06:41 2018

@author: schwerbelastung
"""
#########################################################
### This file is intended for shortening              ###
### the wav files associated with the project.        ###
### The timestamps for start and end of the           ###
### cut audio files have been manually calculated     ###
### from the provided timestamps.                     ###
### The related excel is included in the same folder. ###
#########################################################


import scipy.io.wavfile


fileToShorten_a1 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_1_start_201810211715/device1_channel1_20181021170856.wav")
fileToShorten_b1 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_1_start_201810211715/device1_channel1_20181021180537.wav")

a1_start = 16052400
b1_end = 25092900

shortened_a1 = fileToShorten_a1[1][a1_start:len(fileToShorten_a1[1])]
shortened_b1 = fileToShorten_b1[1][0:len(fileToShorten_b1[1])-b1_end]

scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_1_start_201810211715/a1_short.wav",44100,shortened_a1)
scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_1_start_201810211715/b1_short.wav",44100,shortened_b1)


fileToShorten_a2 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_2_start_201810212330/device1_channel1_20181021232649.wav")
fileToShorten_b2 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_2_start_201810212330/device1_channel1_20181022002331.wav")

a2_start = 8423100
b2_end = 32766300

shortened_a2 = fileToShorten_a2[1][a2_start:len(fileToShorten_a2[1])]
shortened_b2 = fileToShorten_b2[1][0:len(fileToShorten_b2[1])-b2_end]

scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_2_start_201810212330/a2_short.wav",44100,shortened_a2)
scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_2_start_201810212330/b2_short.wav",44100,shortened_b2)


fileToShorten_a3 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_3_start_201810220830/device1_channel1_20181022081553.wav")
fileToShorten_b3 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_3_start_201810220830/device1_channel1_20181022091234.wav")

a3_start = 37352700
b3_end = 3792600

shortened_a3 = fileToShorten_a3[1][a3_start:len(fileToShorten_a3[1])]
shortened_b3 = fileToShorten_b3[1][0:len(fileToShorten_b3[1])-b3_end]

scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_3_start_201810220830/a3_short.wav",44100,shortened_a3)
scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_3_start_201810220830/b3_short.wav",44100,shortened_b3)


fileToShorten_a4 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_4_start_201810230800/device1_channel1_20181023075259.wav")
fileToShorten_b4 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_4_start_201810230800/device1_channel1_20181023084940.wav")

a4_start = 18566100                       
b4_end = 22623300
                                         
shortened_a4 = fileToShorten_a4[1][a4_start:len(fileToShorten_a4[1])]
shortened_b4 = fileToShorten_b4[1][0:len(fileToShorten_b4[1])-b4_end]

scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_4_start_201810230800/a4_short.wav",44100,shortened_a4)
scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_4_start_201810230800/b4_short.wav",44100,shortened_b4)


fileToShorten_a5 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_5_start_201810251530_stopped/device1_channel1_20181025152315.wav")
fileToShorten_b5 = scipy.io.wavfile.read("/Users/schwerbelastung/Desktop/Incidents/Original_not_trimmed/Incident_5_start_201810251530_stopped/device1_channel1_20181025161956.wav")

a5_start = 17860500                                 
b5_end = 23328900
                                         
shortened_a5 = fileToShorten_a5[1][a5_start:len(fileToShorten_a5[1])]
shortened_b5 = fileToShorten_b5[1][0:len(fileToShorten_b5[1])-b5_end]

scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_5_start_201810251530_stopped/a5_short.wav",44100,shortened_a5)
scipy.io.wavfile.write("/Users/schwerbelastung/Desktop/Incidents/Trimmed/Incident_5_start_201810251530_stopped/b5_short.wav",44100,shortened_b5)

#####################################

