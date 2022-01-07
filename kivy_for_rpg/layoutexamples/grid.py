
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
    pass

class Layout2(GridLayout):
    pass

class GridApp(App):
    def build(self):
        return Layout2()



if __name__ == "__main__":
    app = GridApp()
    app.run()
