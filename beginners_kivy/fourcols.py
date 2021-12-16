from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Welcome_Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Welcome_Screen, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))
        self.add_widget(Label(text = "item 1"))

class MyApp(App):
    def build(self):
        return Welcome_Screen()

if __name__ == '__main__':
    MyApp().run()
