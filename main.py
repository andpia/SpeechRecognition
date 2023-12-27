####################################
# Required Packages:
#   * SpeechRecognition
#   * PyAudio
####################################

import speech_recognition as sr

recognizer = sr.Recognizer()

# Acquisisci l'audio dal microfono
with sr.Microphone() as source:
    print("Di qualcosa...")
    try:
        audio_data = recognizer.listen(source)
    except sr.WaitTimeoutError:
        print("Nessun audio rilevato entro il timeout.")

# Usa il riconoscitore per ottenere il testo
try:
    text = recognizer.recognize_google(audio_data, language="it-IT")
    print("Testo riconosciuto:", text)
except sr.UnknownValueError:
    print("Il riconoscitore non ha compreso l'audio.")
except sr.RequestError as e:
    print(f"Errore nella richiesta al servizio di riconoscimento vocale; {e}")
