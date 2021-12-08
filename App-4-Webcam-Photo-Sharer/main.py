import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    # add class name within <class_name> in frontend.kv file
    def search_image(self):
        pass


class RootWidget(ScreenManager):
    # It is there to manage the multiple screen we have, even if it is only one
    # No. of screen classes is equal to number of screen in application
    pass


class MainApp(App):

    def build(self):
        # Actually kivy expects us to have build function
        return RootWidget()


MainApp().run()
