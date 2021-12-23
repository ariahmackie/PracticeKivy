from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp


class LoginScreen(FloatLayout):
    pass


class LoginApp(MDApp):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    LoginApp().run()
