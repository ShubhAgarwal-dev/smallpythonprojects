# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# to get image
from wikipedia import page
import requests

# to get extension of the image received
from os.path import splitext

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    #   # add Screen class name within <class_name> in frontend.kv file
    # -> root in frontend.kv is equal to FirstScreen()

    @staticmethod
    def get_image(query):
        image_link = page(query).images[0]
        return image_link

    @staticmethod
    def download_image(query):
        image_link = FirstScreen.get_image(query)
        response = requests.get(image_link)
        ext = splitext(image_link)[-1].lower()
        with open(fr'files/{query}{ext}', mode='wb') as file:
            file.write(response.content)
        return fr'files/{query}{ext}'

    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        # Get user query from text input
        print('working...')
        self.manager.current_screen.ids.img.source = self.get_image(query)
        # id: img defined in frontend.kv
        # Display the output
        print(self.get_image(query))
        print(type(self.get_image(query)))


class RootWidget(ScreenManager):
    # It is there to manage the multiple screen we have, even if it is only one
    # No. of screen classes is equal to number of screen in application
    pass


class MainApp(App):

    def build(self):
        # Actually kivy expects us to have build function
        return RootWidget()


MainApp().run()
