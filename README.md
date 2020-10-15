In this exercise we have implemented an 8 Bands FIR analysis and synthesis filter bank.

# In analysis-filterbank.py we have
	Created 8 filters using scipy.signal.remez function
	Read an audio file
	Applied the filterbank on the audio
	Plotted the frequency response of each filter

# In upsample-synthesis.py we have
	Taken the same filter bank and audio file
	Applied the filter bank on the audio 
	Downsampled the filterd signals
	Upsampled the signals by inserting zeros
	Applied filter on upsampled signals
	Added all the signals to get the reconstructed audio

# Usage
python analysis-filterbank.py to simply filter the signal and see the plot of filter bank
python upsample-synthesis.py to apply the analysis and synthesis on the audio file