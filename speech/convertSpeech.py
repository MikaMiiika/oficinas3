import speech_recognition as sr
import unidecode

def ConvertSpeech(speech, language="pt-BR"):
    recognizer = sr.Recognizer()
    source = sr.AudioFile(speech)
    with source as s:
        recognizer.adjust_for_ambient_noise(s)
        audio = recognizer.record(s)

    try:
        text = recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        text = "Não entendi"

    return unidecode.unidecode(text)