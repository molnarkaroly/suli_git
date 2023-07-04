import toga
from toga.style import Pack
import socket

client_socket = socket.socket()
client_socket.connect(('192.168.1.103', 12345)) #kintigép 12



class ExampleApp(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a box to hold the input widgets
        input_box = toga.Box(style=Pack(direction='column', padding=5,background_color=toga.constants.BLACK))

        # Create a text label
        self.label = toga.Label('Console:')

        self.selection_input = toga.Selection(items=["-Válassz a listából-",'web', 'program'] , on_select=self.on_select_input_change)

        # Create a text input widget
        self.text_input = toga.TextInput(style=Pack(flex=1))

        # Create a multiline text box
        self.text_box = toga.MultilineTextInput(readonly=True, style=Pack(flex=1,background_color=toga.constants.BLACK, color='lightgreen',font_size=15))

        # Create an OK button
        self.ok_button = toga.Button('OK', on_press=self.ok_pressed, style=Pack(padding=(0, 5)))

        # Add the label, text input, text box and button to the box
        input_box.add(self.label)
        input_box.add(self.text_box)
        input_box.add(self.text_input)        
        input_box.add(self.selection_input)
        input_box.add(self.ok_button)



        # Add the box to the window
        self.main_window.content = input_box

        # Show the main window
        self.main_window.show()

    def ok_pressed(self, widget):
        # Get the text from the text input
        text = self.text_input.value
        self.text_input.value = ""

        if text != "":
            print(text)
            self.text_box.value += text + '\n'
            message = text
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")

       
    def on_select_input_change(self, widget):
        text = self.selection_input.value
        
        if text != "-Válassz a listából-":
            print(text)
            self.text_box.value += text + '\n'
            message = text
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")
            self.selection_input.value = self.selection_input.items[0]
            self.selection_input.value = "-Válassz a listából-"



def main():
    return ExampleApp('CMD_control', 'org.beeware.example')


if __name__ == '__main__':
    main().main_loop()







    

