from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class TwoBackgrounds(FloatLayout):
    pass


class TwoBackgroundsApp(App):
    def build(self):
        return TwoBackgrounds()


if __name__ == "__main__":
    TwoBackgroundsApp().run()
