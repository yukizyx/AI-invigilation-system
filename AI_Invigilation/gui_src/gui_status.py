import PySimpleGUI as sg
import time

class FullScreenWindow:
    def __init__(self):
        # Get the screen resolution
        screen_width, screen_height = sg.Window.get_screen_size()

        # Define the layout of the UI
        layout = [
            [sg.Column([[sg.Text("Current time:" + time.strftime('%H:%M:%S'), font=('Helvetica', 50), justification='center', key='Time', text_color='white')]], element_justification='center', justification='center', expand_x=True)],
            [sg.Column([[sg.Text("Time Left:" + time.strftime('%H:%M:%S'), font=('Helvetica', 50), justification='center', key='Time2', text_color='white')]], element_justification='center', justification='center', expand_x=True)],
            [sg.Column([[sg.Text('CS 4ZP6 Exam', font=('Helvetica', 20), justification='center', text_color='white')]], element_justification='center', justification='center', expand_x=True)]
        ]
        # Create the window

        self.window = sg.Window('Full Screen Window', layout, location=(0, 0), size=(int(screen_width*.9), int(screen_height*.9)), auto_close=False, auto_close_duration=None, finalize=True)

    def run(self):
        # Loop through events

        while True:
            event, values = self.window.read(timeout=1000)

            # If the user closes the window or presses the 'q' key, exit the program
            if event == sg.WINDOW_CLOSED or event == 'q':
                break

            # Update the time
            self.window.find_element('Time').Update("Current time:" + time.strftime('%H:%M:%S'))
            self.window.find_element('Time2').Update("Time Left:" + time.strftime('%H:%M:%S'))
            self.window.refresh()

        # Close the window
        self.window.close()

if __name__ == '__main__':
    program = FullScreenWindow()
    program.run()