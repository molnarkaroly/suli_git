import speech_recognition as sr
import keyboard
import os


# létrehozunk egy SpeechRecognition objektumot
r = sr.Recognizer()

# felvesszük az audio bemenetet a mikrofonról
with sr.Microphone() as source:
    print("Kérlek, beszélj...")
    audio = r.listen(source)

# felismerjük a beszédet
try:
    text = r.recognize_google(audio, language='hu-HU')
    print("A felismert szöveg: " + text)
except sr.UnknownValueError:
    print("Nem tudtam felismerni a beszédet.")
except sr.RequestError as e:
    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
       
if text =="leállítás":
        print("Biztos vagy benne??")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Kérlek, beszélj...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='hu-HU')
                print("A felismert szöveg: " + text)
            except sr.UnknownValueError:
                print("Nem tudtam felismerni a beszédet.")
            except sr.RequestError as e:
                print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        if text == "igen":
            print("Bye!")
        elif text == "nem":
            print("Akkor nem ")

if text == "papagáj":
     os.system('cmd/c "curl parrot.live"')

if text not in ["papagáj", "leállítás","igen", "nem"]:
    print("nem ismerem ezt a parancsot")

