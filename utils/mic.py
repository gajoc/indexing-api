import speech_recognition as sr


def await_for_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say one of the commands: data, copy, next, not clear!')
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


def get_voice_command():
    command = await_for_voice_command()
    while not command:
        print('Please repeat command!')
        command = await_for_voice_command()

    return command
