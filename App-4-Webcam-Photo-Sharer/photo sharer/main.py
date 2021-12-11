# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# to share file across
from fs import FileSharer

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    # Using it as Webcam Class

    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


# For Description for each of this look into photo searcher for the code
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()