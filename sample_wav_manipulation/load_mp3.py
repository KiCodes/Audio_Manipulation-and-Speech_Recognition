from pydub import AudioSegment

# loading and manipulating an audio file

# if mp3 then from_mp3
audio = AudioSegment.from_wav("audios_n_txt/speech_recog.wav")

# increase volume by 6db
audio = audio + 6

# repeat the clip two times
audio = audio * 2

# fade in fade out clip
audio = audio.fade_in(2000)

# export audio in another format and name
audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
