# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

RECOGNIZER = sr.Recognizer()

def recognnize_audio():
    
    ## TODO: Not working properly
    
    """obtain audio from the microphone and recognize speech using Sphinx"""

    with sr.Microphone() as source:
        print("Say something!")
        audio = RECOGNIZER.listen(source)
    print(type(audio))
    
    try:
        print("Sphinx thinks you said " + RECOGNIZER.recognize_sphinx(audio,language = "hi-IN"))
        return audio
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        return "bad request"
    

def audio_to_text():
    """recognize speech using Google Speech Recognition"""
    
    audio = recognnize_audio()
    
    if audio == 'bad request' or audio == '':
        raise sr.RequestError
    
    else:
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `RECOGNIZER.recognize_google(audio)`
            extracted_text =  RECOGNIZER.recognize_google(audio,language="hi-IN")
            print("Google Speech Recognition thinks you said " + extracted_text)
            return extracted_text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    
    audio_to_text()