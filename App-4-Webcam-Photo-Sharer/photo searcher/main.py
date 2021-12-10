# To Develop frontend
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# to get image
from wikipedia import page
import wikipedia
from urllib.request import urlretrieve
# requests module was not giving responding with image rather with

# to choose one option in case of wikipedia.exceptions.DisambiguationError
from random import randint

# to get extension of the image received
from os.path import splitext

kivy.require('2.0.0')
Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    #   # add Screen class name within <class_name> in frontend.kv file
    # -> root in frontend.kv is equal to FirstScreen()

    @staticmethod
    def get_image(query):
        while True:
            try:
                image_link = page(title=query).images[0]
            except wikipedia.exceptions.PageError as err:
                print('Requested page is not found')
                raise err
            except wikipedia.exceptions.DisambiguationError as err:
                # to choose
                num = randint(0, len(err.options))
                query = err.options[num]
                continue
            else:
                break
        return image_link

    @staticmethod
    def download_image(query):
        image_link = FirstScreen.get_image(query)
        ext = splitext(image_link)[-1].lower()
        urlretrieve(image_link, fr'files\{query}{ext}')
        return fr'files/{query}{ext}'

    def set_image(self):
        query = self.manager.current_screen.ids.user_query.text
        # Get user query from text input
        print('working...')
        self.manager.current_screen.ids.img.source = FirstScreen.download_image(
            query)
        # id: img defined in frontend.kv
        # Display the output


class RootWidget(ScreenManager):
    # It is there to manage the multiple screen we have, even if it is only one
    # No. of screen classes is equal to number of screen in application
    pass


class MainApp(App):

    def build(self):
        # Actually kivy expects us to have build function
        return RootWidget()


MainApp().run()
