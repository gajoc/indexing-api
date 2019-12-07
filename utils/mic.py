import speech_recognition as sr


def await_for_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Powiedz co robimy? dane / kopia / następny / nieczytelny')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        voice_command = r.recognize_google(audio, language='pl')
        if voice_command:
            voice_command = voice_command.lower()
        print(f'Google twiedzi, że powiedziałeś {voice_command}.')
        return voice_command
    except sr.UnknownValueError:
        print("Google nie zrozumiało tego co powiedziałeś.")
        return
    except sr.RequestError as e:
        print("Mamy problem, nie można odebrać wyników z Google Speech Recognition service; {0}".format(e))
        return


def get_voice_command():
    command = await_for_voice_command()
    while not command:
        print('Powtórz proszę jeszcze raz!')
        command = await_for_voice_command()

    return command
