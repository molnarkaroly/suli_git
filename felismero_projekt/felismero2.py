import speech_recognition as sr
import keyboard
import os
import time
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#hang növelése vagy csökkentése
def add_system_volume(volume_change):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_object = interface.QueryInterface(IAudioEndpointVolume)
    current_volume = volume_object.GetMasterVolumeLevelScalar()
    new_volume = current_volume + volume_change / 100.0 # hozzáadja a változást a jelenlegi hangerőhöz
    volume_object.SetMasterVolumeLevelScalar(new_volume, None)

# hang beállítása
def set_system_volume(volume):
    volume = volume / 100.0 # konvertálja a százalékos értéket a 0 és 1 közötti értékre
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_object = interface.QueryInterface(IAudioEndpointVolume)
    volume_object.SetMasterVolumeLevelScalar(volume, None)

def print_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_object = cast(interface, POINTER(IAudioEndpointVolume))
    volume = volume_object.GetMasterVolumeLevel()
    print("System volume:", volume)

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
         break
    
    if text not in ["papagáj", "leállítás","igen", "nem", "vége","zene", "help", "játék", "leír","discord","amőba","Google","tab", "enter","hang fel","hang le","hang érték","hang"]:
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
        
    jatekok =["amőba", ]
    if text == "játék":
        print("Mit szeretnél játszani?...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print(f'Válassz egy játékot... \n {jatekok} ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        if text not in jatekok:
            print("nem ismerem ezt a hátékot válasz másikat :D ...")
            print(f'A választható játékok: {jatekok}')
        else:
            if text =='amőba':
                from amöba.twoplayer import *
                continue
            if text =='discord':
                os.system('cmd/c' 'start C:\\Users\\molna\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe')
                continue
    
    programok = ["discord", "Google","YouTube"]
    if text =="program":
        print("Mit szeretnél használni?...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print(f'Válassz egy programot... \n {programok} ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        if text not in programok:
            print("nem ismerem ezt a hátékot válasz másikat :D ...")
            print(f'A választhatá játékok: {programok}')
        else:
            if text =="discord":
                os.system('cmd/c' 'start C:\\Users\\molna\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe')
                continue
            if text == "Google":
                os.system('cmd/c' 'start C:\\Users\\molna\\AppData\\Local\\Google\\Chrome\\Application\chrome.exe')
            if text == "YouTube":
                os.system('cmd/c' 'start C:\\Users\molna\\AppData\\Local\\Google\\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=agimnkijcaahngcdmfeangaknmldooml')

    if text == "tab":
        keyboard.press('tab')

    if text == "enter":
        keyboard.press('enter')

    if text == "hang fel":
        add_system_volume(10)

    if text == "hang le":
        add_system_volume(-10)

    if text =="hang érték":
        print("Mi legyen a beállított hangerő?...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Érték...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
                if isinstance(int(text), (int,float)):
                    set_system_volume(int(text))
                else:
                    continue

    if text =="hang":
        print_system_volume()

