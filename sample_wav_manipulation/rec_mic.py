import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    # things to be captured in the stream recording
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("start recording")

# record for a number of seconds
seconds = 9
frames = []
# reading 3200 frames per iteration
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("audios_n_txt/output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
# write all frames to binary with b"" to create a binary string
obj.writeframes(b"".join(frames))
obj.close()
