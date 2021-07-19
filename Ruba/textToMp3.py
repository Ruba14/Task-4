from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/e0918dc5-688c-4409-ba49-96ecc1cebe87'
apikey = 'W0CPoEKYqlJlANhfrihsEDg7QNSTw-mDzidY5txbDYUY'


def main():

    # Setup Service
    authenticator = IAMAuthenticator(apikey)
    # New TTS Service
    tts = TextToSpeechV1(authenticator=authenticator)
    # Set Service URL
    tts.set_service_url(url)

    with open('text.txt', 'r') as f:
        text = f.read()

    with open('voice.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3',
                             voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)


if __name__ == "__main__":
    main()
