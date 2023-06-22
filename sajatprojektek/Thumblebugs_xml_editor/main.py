import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import tkinter as tk
from tkinter import messagebox
from toga.constants import CENTER
from xml_editor import change_lives_value
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
xml_files = []

for filename in os.listdir(folder_path):
    if filename.endswith('.xml') and 'Arcade' in filename:
        xml_files.append(filename.replace('Arcade.xml',''))

print(xml_files)

class ExampleApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

    
        self.label_jatekos_nev = toga.Label('Válaszd ki a játékos nevét: ', style=Pack(font_size=25))
        main_box.add(self.label_jatekos_nev)

        self.text_input = toga.Selection(items=[ i for i in xml_files], on_select=self.on_text_input_change, style=Pack(font_size=25))
        main_box.add(self.text_input)

        self.label_jatekos_benev = toga.Label('\n\n\n', style=Pack(font_size=25))
        main_box.add(self.label_jatekos_benev)

        self.number_input = toga.NumberInput(min_value=1, max_value=100, value=50, step=1, on_change=self.on_number_input_change,style=Pack(font_size=15))
        main_box.add(self.number_input)

        self.slider = toga.Slider(range=(1, 100), value=50, on_change=self.on_slider_change)
        main_box.add(self.slider)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.label = toga.Label('Lives value: 50\n\n', style=Pack(font_size=20))
        main_box.add(self.label)

        self.Gomb_OK1 = toga.Button('OK', style=Pack(font_size=25), on_press=self.gombok1)
        main_box.add(self.Gomb_OK1)



    def on_text_input_change(self, widget):
        self.label_jatekos_benev.text ='\nA kiválasztott játékos: ' + widget.value +'\n\n'


    def on_slider_change(self, widget):
        self.label.text = f'Live value: {int(widget.value)}\n\n'
        self.number_input.value = int(widget.value)
        


    def on_number_input_change(self, widget):
        self.slider.value = widget.value
        print(widget.value)

    def gombok1(self, widget):
        if self.text_input.value != "":
            print(f'A beállítandó élet érték: {int(self.number_input.value)}')
            print(f'A játékos neve: {self.text_input.value}')
            try:
                change_lives_value(int(self.number_input.value), self.text_input.value)
                self.main_window.close()

            except:
                tk.Tk().withdraw()
                messagebox.showerror("Hiba", "Hibás bemenet")
        else:
            tk.Tk().withdraw()
            messagebox.showerror("Hiba", "Helytelen bemenet")
        

def main():
    return ExampleApp('Thumblebugs_2_xml_editor', 'org.beeware.example')


if __name__ == '__main__':
    main().main_loop()