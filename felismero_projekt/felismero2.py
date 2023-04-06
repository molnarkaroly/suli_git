import speech_recognition as sr
import keyboard
import os
import time

while True:  
 # létrehozunk egy SpeechRecognition objektumot
    r = sr.Recognizer()
    
    # felvesszük az audio bemenetet a mikrofonról
    with sr.Microphone() as source:
        print("Start?...")
        audio = r.listen(source)
    
    # felismerjük a beszédet
    try:
        text = r.recognize_google(audio, language='hu-HU')
        print("A felismert szöveg: " + text)
    except sr.UnknownValueError:
        print("Nem tudtam felismerni a beszédet.")
        continue
    except sr.RequestError as e:
        print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        continue

    if text =="be":
        break

while True:  
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
        continue

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
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
            if text == "igen":
                print("Bye!")
                break
            elif text == "nem":
                print("Akkor nem ")
                continue
    
    if text == "papagáj":
         os.system('cmd/c "curl parrot.live"')
    
    if text not in ["papagáj", "leállítás","igen", "nem", "vége","zene", "help", "leír"]:
        print("nem ismerem ezt a parancsot")
    
    if text == "vége":
        break
    
    if text == "zene":
        os.system('cmd/c "start https://music.youtube.com/watch?v=IC25CJxV3yc&feature=share"')


    if text == "help":
        os.system('cmd/c "start https://chat.openai.com/chat"')
        time.sleep(15)
        keyboard.write('Szia')
        keyboard.press('Enter')
        continue

    if text == "leír":
        print("mit szeretnél hogy le írjak?")

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Írás....")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        keyboard.write(text)
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Enter?...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
                
        if text =="igen":
            keyboard.press("Enter")
            continue            
        else:
            continue
        

