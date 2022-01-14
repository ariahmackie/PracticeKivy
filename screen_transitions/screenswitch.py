import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Home(Screen):
    pass

class Profile(Screen):
    pass

class Login(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass



presentation = Builder.load_file("windowmanager.kv")
class WindowManager(App):
    def build(self):
        return presentation
WindowManager().run()
