#pip install argparse
#pip install numpy
#pip install scipy
import argparse
import numpy
import scipy.io.wavfile


parser = argparse.ArgumentParser("WavToCsv")
parser.add_argument("PathToWav", help="Full path to WAV file, CSV will be output as 'csv' or 'npy' with the same name")
parser.add_argument("TargetType", help="Target file type 'csv' (textual csv - slower) or 'npy' (binary numpy - faster)")
args = parser.parse_args()

a = scipy.io.wavfile.read(args.PathToWav)
b = numpy.array(a[1],dtype=float)
if (args.TargetType == 'csv'):
	numpy.savetxt(args.PathToWav+'.csv', b, delimiter=",")
elif (args.TargetType == 'npy'):
	numpy.save(args.PathToWav+'.npy', b)
else:
	parser.print_help()