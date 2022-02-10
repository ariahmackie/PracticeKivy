from kivymd.app import MDApp
from kivy.uix.widget import Widget


class Rootwidget(Widget):
        pass

class ProgressApp(MDApp):
    def build(self):
        return Rootwidget()


if __name__ == '__main__':
    ProgressApp().run()
