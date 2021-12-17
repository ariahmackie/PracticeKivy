from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class MyRelativeLayout(RelativeLayout):
	pass

class DrawingWindow(App):
	def build(self):
		return MyRelativeLayout()


if __name__ == "__main__":
	window = DrawingWindow()
	window.run()
