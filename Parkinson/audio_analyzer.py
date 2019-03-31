from pyAudioAnalysis import audioBasicIO, audioFeatureExtraction
import numpy as np


class AudioAnalyze:

    def __init__(self, filename):
        [Fs, x] = audioBasicIO.readAudioFile(filename)
        F = audioFeatureExtraction.stFeatureExtraction(
            np.mean(x, axis=1) if x.ndim == 2 else x, Fs, 0.050*Fs, 0.025*Fs)
        # print (F[0][1])
        self.input_from_audio = F[0][1]

    def slice_audio_parameters(self):
        value = self.input_from_audio[:19]
       # print(np.transpose(np.reshape(value, (-1, 19))))
        value = np.reshape(value, (-1, 19))
        #value = np.transpose(value)
        return value


"""
obj = AudioAnalyze("sample.wav")
value = obj.slice_audio_parameters()
"""