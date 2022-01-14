from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class ScrollButtons(ScrollView):
    pass

class Scroll(App):
    def build(self):
        return ScrollButtons()


if __name__ == "__main__":
    scrollclass = Scroll()
    scrollclass.run()
