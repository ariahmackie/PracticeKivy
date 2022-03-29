from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = (400,800)

class LoginScreen(FloatLayout):
    pass

class HomeScreen(FloatLayout):
    pass


class LoginApp(MDApp):
    def build(self):
        return LoginScreen()

    def process(self):
        email = self.root.ids.email.text
        password = self.root.ids.password.text
        print(email)
        print(password)


if __name__ == "__main__":
    LoginApp().run()
