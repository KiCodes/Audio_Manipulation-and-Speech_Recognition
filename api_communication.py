import time
import requests
from api_config import API_KEY_ASSEMBLYAI

# 4 parts to speech recognition

# 1 upload file we have locally to assembly ai

# uploading a file is making a POST request needed to send to upload endpoint,
# api key in headers, and the data(file that is read, needed to be in chunk sizes mega bites)


upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY_ASSEMBLYAI}


def upload(filename):
    # upload to assemblyAI using requests, API key and filename
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                                    headers=headers,
                                    data=read_file(filename))

    # extract audio url from json response
    audio_url = upload_response.json()['upload_url']  # 'upload_url' gotten from printing out the response.json()
    return audio_url


# 2 transcription
def transcribe(url_audio):
    # send a post request for transcription using the uploaded audio url
    transcript_request = {"audio_url": url_audio}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    # getting the id from the json response
    job_id = transcript_response.json()['id']
    return job_id


# 3 keep polling assembly ai transcription to see if the transcription is done
# from sending to transcription we get the id amongst other data that will help us keep checking if the job is done
def poll(transcribe_id):
    # p.e is specific to the the transcription
    polling_endpoint = transcript_endpoint + '/' + transcribe_id
    # get information from API
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url_audio):
    transcribe_id = transcribe(url_audio)
    # loop to continuously send get request to assemblyAI until the status request turns from processing to completed
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print("waiting 30 seconds...")
        time.sleep(30)


# 4 save transcript
def saved_transcript(url_audio, filename):
    data, error = get_transcription_result_url(url_audio)

    if data:
        text_filename = filename + '.txt'
        with open(text_filename, "w") as f:
            # write json text data received from get request to text file
            f.write(data['text'])
        print("transcription saved")
    elif error:
        print("error", error)
