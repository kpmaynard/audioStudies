"""
Input:
inputFile: file path to the wav file
Output:
A tuple of the minimum and the maximum value of the audio
samples, like: (min_val, max_val)
"""

from scipy.io.wavfile import read

import numpy as np

import sys


def minMaxAudio(inputFile):

	sys.path.append('/home/vagrant/sms-tools/software/models')

	import utilFunctions as UF


	(fs, x) = UF.wavread(inputFile)
	min_val = np.min(x)
	max_val = np.max(x)	
	return(min_val, max_val)

