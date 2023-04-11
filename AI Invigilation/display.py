import PySimpleGUI as sg
import cv2
import io
from PIL import Image

class ImageGUI:
    def __init__(self):
        self.layout = [
            [sg.Image(filename='', key='image_display', size=(800, 600))],
            [
                sg.Button('<<<', key='left_button', image_subsample=2),
                sg.Button('>>>', key='right_button', image_subsample=2)
            ]
        ]

        self.window = sg.Window('Image Display', self.layout, finalize=True)

    def display_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)

        max_width, max_height = 800, 600
        img_width, img_height = img_pil.size

        # Calculate aspect ratio
        aspect_ratio = float(img_width) / float(img_height)

        # Calculate new dimensions
        if img_width > max_width or img_height > max_height:
            if aspect_ratio > 1:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
        else:
            new_width, new_height = img_width, img_height

        # Resize and center the image
        img_pil = img_pil.resize((new_width, new_height), Image.ANTIALIAS)
        img_bg = Image.new('RGB', (max_width, max_height), (0, 0, 0))
        img_bg.paste(img_pil, ((max_width - new_width) // 2, (max_height - new_height) // 2))

        bio = io.BytesIO()
        img_bg.save(bio, format='PNG')
        img_bytes = bio.getvalue()

        self.window['image_display'].update(data=img_bytes)

    def event_loop(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'left_button':
                print("Left button clicked")
                # Add your logic here

            if event == 'right_button':
                print("Right button clicked")
                # Add your logic here

        self.window.close()

if __name__ == "__main__":
    gui = ImageGUI()

    # Load an image as a numpy array (replace 'sample_image.jpg' with your image file)
    img = cv2.imread('sample_image.png')
    gui.display_image(img)

    gui.event_loop()