import tkinter as tk
import time
import os


# Létrehozzuk a fő ablakot
root = tk.Tk()
root.title("Időzítő")
root.geometry("170x200")
root.resizable(False, False)
root.config(bg="#6e6e6e")


# Létrehozzuk a beviteli mezőket az óra, perc és másodperc értékek bekérésehez
hours_entry = tk.Entry(root)
minutes_entry = tk.Entry(root)
seconds_entry = tk.Entry(root)
ora = tk.Label(root, text="Óra")
perc = tk.Label(root, text="Perc")
másodperc = tk.Label(root, text="Másodperc")


hours = 0
minutes = 0
seconds = 0

# Létrehozzuk a "Start" gombot, amely elindítja a visszaszámlálást
def start():
  # Beolvassuk az óra, perc és másodperc értékeket
  hours = int(hours_entry.get())
  minutes = int(minutes_entry.get())
  seconds = int(seconds_entry.get())

  # Számoljuk ki az összesen hány másodperc
  total_seconds = hours * 3600 + minutes * 60 + seconds

  

  # Visszaszámolunk a megadott időig
  while total_seconds > 0:
    # Megjelenítjük az aktuális időt
    time_label["text"] = f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}"
    root.update()

    # Várunk 1 másodpercet
    time.sleep(1)

    # Csökkentjük az összes másodperc számát 1-el
    total_seconds -= 1

    if total_seconds <= 0:
        time_label["text"] = "00:00:00"
        os.system('cmd/c "shutdown"') # Shutdown "/h"
        root.destroy()

start_button = tk.Button(root, text="Start", command=start)

# Létrehozzuk a címkét az aktuális idő megjelenítéséhez
time_label = tk.Label(root, text="00:00:00", font=("Digital-7", 30))

# Elrendezzük az elemeket az ablakban
ora.pack()
hours_entry.pack()
perc.pack()
minutes_entry.pack()
másodperc.pack()

seconds_entry.pack()
start_button.pack()
time_label.pack()


# Futtatjuk az ablakot
root.mainloop()