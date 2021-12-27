from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (400,800)

class LoginScreen(FloatLayout):
    pass


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    LoginApp().run()
