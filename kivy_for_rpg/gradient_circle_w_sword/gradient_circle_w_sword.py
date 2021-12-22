import kivy
from kivy.app import App
from kivy.uix.widget import Widget





class DrawCircle(Widget):
    pass


class CircleApp(App):
    def build(self):
        return DrawCircle()


if __name__ == "__main__":
    CircleApp().run()
