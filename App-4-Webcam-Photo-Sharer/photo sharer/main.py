# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


# For Description for each of this look into photo searcher for the code
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp()