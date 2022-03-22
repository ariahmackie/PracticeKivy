from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    pass

class BoxApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    app = BoxApp()
    app.run()
