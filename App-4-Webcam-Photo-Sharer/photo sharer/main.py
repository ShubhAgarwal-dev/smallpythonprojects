# type: ignore
# pyright: reportMissingModuleSource=false
# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

# to share file across
from filesharer import FileSharer

# to make unique files
import time

# to open link in the browser
import webbrowser

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    # Using it as Webcam Class

    def __call__(self):
        '''
        To stop the camera in the beginning, as it did reduce the glitch
        '''
        self.ids.camera.play = False

    def start(self):
        """
        To start the camera and change the button
        """
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera_button.text = 'Stop Camera'

    def stop(self):
        '''
        To stop the camera and change the button
        '''
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.camera_button.text = 'Start Camera'

    def capture(self):
        """
        Captures the image on the webcam and  saves it to capture folder
        with current date-time as filename.
        """

        current_time = time.strftime("%Y%m%d-%M%H%S")
        self.file_path = fr'capture\{current_time}.png'
        # added self to make it a instance attribute so it could be accessible in other screens

        self.ids.camera.export_to_png('image.png')
        self.ids.camera.export_to_png(self.file_path)

        print('capture')

        self.manager.current = 'image_screen'  # it is the name of the screen not the id
        self.manager.current_screen.ids.img.source = 'image.png'


class ImageScreen(Screen):
    url_not_found_message = 'Create a link first'

    def create_link(self):
        '''
        Access the photo filepath, creates a sharable link of the image and
        display it on the label
        '''
        image_path = 'image.png'
        # Rather we could have also used
        ## image_path = App.get_running_app().root.ids.camera_screen.file_path
        # we use screen id in the above case

        file_sharer = FileSharer(file_path=image_path)
        self.url = file_sharer.share()
        self.ids.link_label.text = self.url

    def copy_link(self):
        """
        Copies the image url to the clipboard of the device to paste 
        where ever you want it to
        """
        try:
            Clipboard.copy(self.url)
        except AttributeError:
            self.ids.link_label.text = self.url_not_found_message

    def open_link(self):
        '''
        Open the image url on the default browser
        '''
        try:
            webbrowser.open(url=self.url)
        except AttributeError:
            self.ids.link_label.text = self.url_not_found_message


# For Description for each of this look into photo searcher for the code
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()