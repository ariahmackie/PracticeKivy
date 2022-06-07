#based on https://www.geeksforgeeks.org/python-how-to-use-multiple-kv-files-in-kivy/

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("login.kv")
Builder.load_file("home.kv")
Builder.load_file("newtask.kv")

class main_kv(GridLayout):
	pass

class MainApp(App):
	def build(self):
		self.x = 150
		self.y = 400
		return main_kv()
if __name__ == '__main__':
	MainApp().run()
