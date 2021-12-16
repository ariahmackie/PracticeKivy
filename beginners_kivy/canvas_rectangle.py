from kivy.app import App
from kivy.uix.widget import Widget

class Rectangle(Widget):
	pass


class RectangleApp(App):
	def build(self):
		return Rectangle()


if __name__== '__main__':
	RectangleApp().run()
