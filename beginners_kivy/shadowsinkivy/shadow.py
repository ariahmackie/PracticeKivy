from kivy.app import App
from kivy.uix.widget import Widget

class ShadowButtons(Widget):
    pass

class ShadowApp(App):
    def build(self):
        return ShadowButtons()


if __name__ == "__main__":
    ShadowApp().run()
