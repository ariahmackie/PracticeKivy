from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.graphics import Triangle
Window.clearcolor = (0.247, 0.854, 0.952, 1)

class HouseRoof(Widget):
    def __init__(self, **kwargs):
        with self.canvas:
            Color(0.2, 0.8, 0)



class House(Widget):
    pass

class HouseApp(App):
    def build(self):
        return House()


if __name__ == '__main__':
    HouseApp().run()
