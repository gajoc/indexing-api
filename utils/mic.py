import speech_recognition as sr


def await_for_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say `next` to continue or `copy` to attach previous data to current link!')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        voice_command = r.recognize_google(audio, language='en_gb')
        if voice_command:
            voice_command = voice_command.lower()
        print("Google Speech Recognition thinks you said " + voice_command)
        return voice_command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return
