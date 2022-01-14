# https://stackoverflow.com/questions/33817585/kivy-trying-to-get-grid-layout-with-buttons-to-scroll

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

class Screen(GridLayout):
    pass

# this does scrolling with buttons
class ScrollClass(App):
    def build(self):
        Buttonlayout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        Buttonlayout.bind(minimum_height=Buttonlayout.setter('height'))
        btn1 = Button(text = "1", size_hint_y=None, height=50)
        btn2 = Button(text = "2", size_hint_y=None, height =50)
        btn3 = Button(text = "3", size_hint_y=None, height =50)
        btn4 = Button(text = "4", size_hint_y=None, height =50)
        btn5 = Button(text = "5", size_hint_y=None, height =50)
        btn6 = Button(text = "6", size_hint_y=None, height =50)
        btn7 = Button(text = "7", size_hint_y=None, height =50)
        Buttonlayout.add_widget(btn1)
        Buttonlayout.add_widget(btn2)
        Buttonlayout.add_widget(btn3)
        Buttonlayout.add_widget(btn4)
        Buttonlayout.add_widget(btn5)
        Buttonlayout.add_widget(btn6)
        Buttonlayout.add_widget(btn7)
        root = ScrollView()
        root.add_widget(Buttonlayout)
        return root

if __name__== "__main__":
    scrollclass = ScrollClass()
    scrollclass.run()
