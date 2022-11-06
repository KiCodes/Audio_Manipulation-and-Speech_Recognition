import wave

# taking a wave file and setting it into a new wave file
obj = wave.open("../audios_n_txt/speech_recog.wav", "rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

# time of audio
t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

# actual frames
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("../audios_n_txt/speech_recog_new.wav", "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()
