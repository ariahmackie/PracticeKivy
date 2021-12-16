from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.clearcolor = (0.247, 0.854, 0.952, 1)

class HouseRoof(Widget):
    triangle = ObjectProperty(None)
    def __init__(self, **kwargs):
        self.triangle = Triangle(points = [ 0, 0, 100, 100, 200, 0] )


class House(Widget):
    pass

class HouseApp(App):
    def build(self):
        return House()


if __name__ == '__main__':
    HouseApp().run()
