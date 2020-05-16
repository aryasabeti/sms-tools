import sys
import os
sys.path.append('../../software/models/')
from utilFunctions import wavread

"""
A1-Part-2: Basic operations with audio

Write a function that reads an audio file and returns the minimum and the maximum values of the audio 
samples in that file. 

The input to the function is the wav file name (including the path) and the output should be two floating 
point values returned as a tuple.

If you run your code using oboe-A4.wav as the input, the function should return the following output:  
(-0.83486432, 0.56501967)
"""
def minMaxAudio(inputFile):
    """
    Input:
        inputFile: file name of the wav file (including path)
    Output:
        A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
    """
    f = wavread(inputFile)
    sound_data = f[1]
    sound_min = min(sound_data)
    sound_max = max(sound_data)

    print(f"min: {sound_min}, max: {sound_max}")
    return sound_min, sound_max

if __name__ == '__main__':
    inputFile = sys.argv[1]
    minMaxAudio(inputFile)

