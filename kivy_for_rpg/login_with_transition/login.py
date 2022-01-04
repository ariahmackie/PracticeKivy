from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

Window.size = (400,800)

class Login(Screen):
    pass

class Home(Screen):
    pass



#presentation = Builder.load_file("login.kv")

class LoginApp(MDApp):
    def build(self):
        sm = ScreenManager(transition = NoTransition())
        sm.add_widget(Login(name='login'))
        sm.add_widget(Home(name='home'))
        return sm

    def process(self):
        email = self.root.ids.email.text
        password = self.root.ids.password.text
        print(email)
        print(password)
        sm.current = "home"


if __name__ == "__main__":
    LoginApp().run()
