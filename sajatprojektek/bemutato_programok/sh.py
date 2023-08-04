import customtkinter as ctk
import time
import os

# Set the appearance mode to dark
ctk.set_appearance_mode("dark")
theme_mode = "dark"

# Create the main window
root = ctk.CTk()
root.title("Időzítő")
root.geometry("170x250")
root.resizable(False, False)

# Create the input fields to enter the hours, minutes and seconds values
hours_entry = ctk.CTkEntry(root)
hours_entry.insert(0, "0")
minutes_entry = ctk.CTkEntry(root)
minutes_entry.insert(0, "0")
seconds_entry = ctk.CTkEntry(root)
seconds_entry.insert(0, "0")
ora = ctk.CTkLabel(root, text="Óra")
perc = ctk.CTkLabel(root, text="Perc")
másodperc = ctk.CTkLabel(root, text="Másodperc")

hours = 0
minutes = 0
seconds = 0

min_st = 1

def start():
    global min_st
    min_st = 1
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())

    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        time_label.configure(text=f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}")
        root.update()

        time.sleep(1)

        if min_st == 1:
            total_seconds -= min_st

        if total_seconds <= 0:
            time_label.configure(text="00:00:00")
            os.system('cmd/c "shutdown"') # Shutdown "/h"
            root.destroy()


def stop():
    global min_st
    if min_st == 1:
        min_st = 0
        stop_button.configure(fg_color="red")
        time_label.configure(fg="red")
    else:
        min_st = 1
        stop_button.configure(fg_color="blue")
        time_label.configure(fg="black")

start_button = ctk.CTkButton(root, text="Start", command=start)
start_button.configure(fg_color="green")
stop_button = ctk.CTkButton(root, text="Stop", command=stop)
stop_button.configure(fg_color="blue")

time_label = ctk.CTkLabel(root, text="00:00:00", font=("Digital-7", 30))

def moon():
    global theme_mode
    if theme_mode == "dark":
        ctk.set_appearance_mode("light")
        theme_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        theme_mode = "dark"

# Create a moon icon and a "Z" text in the top right corner
moon_icon = ctk.CTkButton(root, text="🌙", font=("Arial", 12), command=moon, width=12, height=12)
moon_icon.place(relx=1.0, rely=0.0, anchor=ctk.NE)

# Arrange the elements in the window
ora.pack()
hours_entry.pack()
perc.pack()
minutes_entry.pack()
másodperc.pack()

seconds_entry.pack()
start_button.pack()
stop_button.pack()
time_label.pack()

# Run the window
root.mainloop()
