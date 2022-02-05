from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.textinput import TextInput
class MainBackground(Widget):
    pass

class PopupApp(App):
    def build(self):
        return MainBackground()

if __name__ == "__main__":
    PopupApp().run()
