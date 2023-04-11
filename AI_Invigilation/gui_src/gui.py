import configparser
import threading
import PySimpleGUI as sg
import os
import time

from src.connection_manager import *
from src.video_controller import video_controller
from Auth import start_flask
from gui_src.gui_image import *
from src.image_manager import *
from src.action_queue import *
from src.trigger import *

class ui_main_page:
    def __init__(self, config):
        #initialise connection manager for backend and wi server
        self.be_connection = connection_manager(config['BE_Network']['host'], config['BE_Network'].getint(option='port'))
        self.vc = video_controller(config['File_path']['report_path'], config['File_path']['recording_path'])
        self.cam_count = self.vc.init_camera(config)
        self.sending_thread = None
        self.flask = None
        self.connected = False
        self.imageUI = None
        self.action_queue = ActionQueue()
        self.tm = trigger()
        # Define the layout of the UI
        self.layout = [
            [sg.Text('BE Connection 1:'), sg.InputText(key='status1', disabled=True), sg.Button('Start BE'), sg.Button('Stop BE')],
            [sg.Text('WI Server 2:'), sg.InputText(key='status2', disabled=True), sg.Button('Start WI'), sg.Button('Cam')],
            [sg.Output(size=(80, 10))]
        ]
        # Create the window
        self.window = sg.Window('AI Invigilation Main Machine', self.layout)

    def run(self):
        # Loop through events
        while True:
            event, values = self.window.read(timeout=1000/5)

            if not self.action_queue.is_empty():
                (action, values) = self.action_queue.get_top_action()
                if action == SET_TRIGER:
                    print('Set triger:', values)
                    self.tm.set_trigger(values)
                elif action == SET_CAMERA:
                    print('Set camera:', values)
                self.action_queue.remove_action()

            # If the user closes the window, exit the program
            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Start BE':
                self.window['status1'].update('Connecting...')
                #connect to backend on a separate thread to prevent blocking
                self.window.start_thread(self.be_connection.connect, '-CONNECT-')
            if event == 'Stop BE' and self.connected:
                self.connected = False
                print('Disconnected from backend server')
                self.window['status1'].update('Stopped')
                self.window.Refresh()
                self.be_connection.end_sending()
                self.sending_thread.join()
                self.be_connection.close()

            if event == '-CONNECT-':
                if values['-CONNECT-']:
                    self.connected = True
                    print('Connected to backend server')
                    self.window['status1'].update('Connected')
                    print('Start Recroding and stream to backend server')
                    self.window.Refresh()
                    self.vc.start_Recording()
                    self.sending_thread = threading.Thread(target=self.be_connection.start_sending, args=(self.vc,))
                    self.sending_thread.start()
                else:
                    print('Failed to connect to backend server')
            # Handle events for status 2
            if event == 'Start WI':
                print('Starting flask server')
                self.window['status2'].update('Starting...')
                self.window.Refresh()
                self.flask = threading.Thread(target=start_flask)
                self.flask.start()
                print("Please start react server")
            if event == 'Cam':
                self.imageUI = ImageGUI(self.cam_count)
                self.imageUI.event_loop()
                # fm = self.vc.get_Next_detection_frame()
            # Print output to the console
            self.window.Refresh()

        # Close the window
        self.window.close()

    def update_status1(self, new_status):
        self.window['status1'].update(new_status)

    def update_status2(self, new_status):
        self.window['status2'].update(new_status)

# if __name__ == '__main__':
#     program = ui_main_page()
#     program.run()
