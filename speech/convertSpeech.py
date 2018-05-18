import speech_recognition as sr

def ConvertSpeech(speech, language):
    recognizer = sr.Recognizer()
    source = sr.AudioFile(speech)
    with source as s:
        recognizer.adjust_for_ambient_noise(s)
        audio = recognizer.record(s)

    try:
        text = recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        print("Couldnt recognize")

    return text