# Audio_Manipulation-and-Speech_Recognition
Project by Harold Ekpo

This is a project that demonstrates audio manipulation using matplotlib/numpy and speech recognition AI using AssemblyAI API

in the 'Sample_wav_manipulation' directory we have 4 python files as follows:
1. wave_example: this displays all the metadata that can be accessed about a wave file; the frame rate, number of frames,
    number of channels, sample width and time of the audio. it also demonstrates writing into a new audion file
 
2. rec_mic: demonstrates recording live into an audio file with predestined settings

3. plot_audio: here a graphy is plotting from the audio frequency(read frames) and length of the audio using matplotlib and numpy

4. load_mp3: involves the manipulation of an audion file in terms of volume(in db), repetition, fading in/out and changing file format/extension

The main.py, api_config and api_communication connect to the assemblyAI API in order to upload file to be transcribed, extract url of the audio,
and post it to be transcribed, which then returns a status json amongst other information. The transcribed words are then stored in a text file along with the other
recorded audio in the project (audios_n_txt)