# type: ignore
# pyright: reportMissingModuleSource=false
# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# to share file across
from filesharer import FileSharer

# to make unique files
import time

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    # Using it as Webcam Class

    def __call__(self):
        self.ids.camera.play = False

    def start(self):
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera_button.text = 'Stop Camera'

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.camera_button.text = 'Start Camera'

    def capture(self):
        current_time = time.strftime("%Y%m%d-%M%H%S")
        path = fr'capture\{current_time}.png'

        self.ids.camera.export_to_png('image.png')
        self.ids.camera.export_to_png(path)

        print('capture')


class ImageScreen(Screen):
    pass


# For Description for each of this look into photo searcher for the code
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()