import speech_recognition as sr
import keyboard
import os
import time
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import webbrowser


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

    if text =="vége":
        break


while True:  
    if text == "vége": 
        break
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
    
    if text not in ["papagáj", "leállítás","igen", "nem", "vége","zene", "help", "játék", "leír","discord","amőba","Google","tab", "enter","hang fel","hang le","hang érték","hang","keres","keress","időzített leállítás"]:
        print("nem ismerem ezt a parancsot")
    
    if text == "vége":
        break
    
    if text == "zene":
        r = sr.Recognizer()

        with sr.Microphone() as source:

            try:
                text = r.recognize_google(audio, language='hu-HU')
                print("Milyen dalra van szükséged?")
                audio = r.listen(source)
                song = r.recognize_google(audio, language='hu-HU')
                print("Keresed a következő dalt: " + song)
                webbrowser.open("https://music.youtube.com/search?q=" + song)

            except sr.UnknownValueError:
                print("Nem tudtam felismerni a beszédet.")
            except sr.RequestError as e:
                print("Hiba történt a Google Speech API használatakor; {0}".format(e))




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
        
    jatekok =["amőba", "GTA"]
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
            if text =='GTA':
                os.system('cmd/c' 'start com.epicgames.launcher://apps/0584d2013f0149a791e7b9bad0eec102%3A6e563a2c0f5f46e3b4e88b5f4ed50cca%3A9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true')
                break
    
    programok = ["discord", "Google","YouTube",]
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
                if text == "öt":
                    set_system_volume(5)



    if text =="hang":
        print_system_volume()


    if text =="keres"or text == "keress":
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Mit keressek?...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                
                    webbrowser.open("https://www.google.com/search?q=" + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))


    if text == "időzített leállítás":
        print("Szeretnéd a hangalapú verziót használni?...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
        if text == "nem":
            from shutdown.shutdown import *

            
        if text =="igen":
            shutdown_hour = 0
            shutdown_minute = 0
            shutdown_second = 0
            r = sr.Recognizer()
        with sr.Microphone() as source:
                print("óra...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                    if isinstance(int(text), (int,float)):
                        shutdown_hour=(int(text))
                    if text == "öt":
                        shutdown_hour = 5
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))
                r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Perc...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                    if isinstance(int(text), (int,float)):
                        shutdown_minute=(int(text))
                    if text == "öt":
                        shutdown_minute = 5
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))

                r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Másodperc...")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language='hu-HU')
                    print("A felismert szöveg: " + text)
                    if isinstance(int(text), (int,float)):
                        shutdown_second=(int(text))
                    if text == "öt":
                        shutdown_second = 5
                except sr.UnknownValueError:
                    print("Nem tudtam felismerni a beszédet.")
                    continue
                except sr.RequestError as e:
                    print("Hiba történt a Google Speech API használatakor; {0}".format(e))

                print(f'óra {shutdown_hour} perc {shutdown_minute} másod {shutdown_second}')
                shut_time = (shutdown_hour*3600)+(shutdown_minute*60)+shutdown_second
                print(f'shut_time {shut_time}')

 

                 
                

