import wave
import matplotlib.pyplot as plt
import numpy as np

# plotting a graph of frequency against time for an audio file
obj = wave.open("../audios_n_txt/speech_recog.wav", "rb")

# sample frequency
sample_freq = obj.getframerate()
# number of samples
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()
# time of audio = number of samples / sameple freq
t_audio = n_samples / sample_freq

print(round(t_audio))

# plotting the frequency against time

signal_array = np.frombuffer(signal_wave, dtype=np.int32)

# 0 is start, end is length of signal, sample for each point in time
times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 17))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
