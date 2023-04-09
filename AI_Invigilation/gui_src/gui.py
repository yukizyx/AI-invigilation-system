import configparser

import PySimpleGUI as sg
from src.connection_manager import *


class ui_main_page:
    def __init__(self, config):
        #initialise connection manager for backend and wi server
        self.be_connection = connection_manager(config['BE_Network']['host'], config['BE_Network'].getint(option='port'))

        # Define the layout of the UI
        self.layout = [
            [sg.Text('BE Connection 1:'), sg.InputText(key='status1', disabled=True), sg.Button('Start BE'), sg.Button('Stop BE'), sg.Button('Start Streaming')],
            [sg.Text('WI Server 2:'), sg.InputText(key='status2', disabled=True), sg.Button('Start WI'), sg.Button('Stop WI')],
            [sg.Output(size=(80, 10))]
        ]
        # Create the window
        self.window = sg.Window('AI Invigilation Main Machine', self.layout)

    def run(self):
        # Loop through events
        while True:
            event, values = self.window.read()

            # If the user closes the window, exit the program
            if event == sg.WINDOW_CLOSED:
                break

            # Handle events for status 1
            if event == 'Start BE':
                self.window['status1'].update('Connecting...')
                #connect to backend on a separate thread to prevent blocking
                self.window.start_thread(self.be_connection.connect, '-CONNECT-')
                self.be_connection.connect()
            if event == 'Stop BE' and values['-CONNECT-']:
                print('Disconnected from backend server')
                self.window['status1'].update('Stopped')
                self.be_connection.close()

            if event == '-CONNECT-':
                if values['-CONNECT-']:
                    print('Connected to backend server')
                    self.window['status1'].update('Connected')
                else:
                    print('Failed to connect to backend server')
            # Handle events for status 2
            if event == 'Start 2':
                self.window['status2'].update('Connecting...')
            if event == 'Stop 2':
                self.window['status2'].update('Stopped')

            # Print output to the console
            print(event, values)

        # Close the window
        self.window.close()

    def update_status1(self, new_status):
        self.window['status1'].update(new_status)

    def update_status2(self, new_status):
        self.window['status2'].update(new_status)

# if __name__ == '__main__':
#     program = ui_main_page()
#     program.run()
