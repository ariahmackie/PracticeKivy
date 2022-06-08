#based on https://www.geeksforgeeks.org/python-how-to-use-multiple-kv-files-in-kivy/

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginWindow(Screen):
	pass

class HomeWindow(Screen):
	pass

class NewTaskWindow(Screen):
	pass 

class WindowManager(ScreenManager):
	pass

main = Builder.load_file("main.kv")
home = Builder.load_file("home.kv")
newtask = Builder.load_file("newtask.kv")

class MainApp(App):
	def build(self):
		return main

if __name__ == '__main__':
	MainApp().run()
