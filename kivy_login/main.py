from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
#import pandas as pd  import pandas later

# popup function class
class PopupWindow(Widget):
	def btn(self):
		pop_function()

# gui
class GuiPopUp(FloatLayout):
	pass

def pop_function():
	show = GuiPopUp()
	window =  Popup(title = "popup", content = show, size_hint = (None, None), size = (300, 300)) 
	window.open()

# class to accept user and validate it
class LoginWindow(Screen):
	email = ObjectProperty(None)
	password = ObjectProperty(None)
	def validate(self):
	# validate if the email already exists
		if self.email.text not in users['Email'].unique()
			pop_function()
		else:                   # switching the current screen to display validation result
			sm.current = 'logdata'
			# reset TextInput widget
			self.email.text = ""
			self.password.text = ""

class SignUpWindow(Screen):
	""" class to accept sign up info """
	name2 = ObjectProperty(None)
	email = ObjectProperty(None)
	password = ObjectProperty(None)
	def signup_btn(self):
		"""creating a  dataframeo of the info"""
		user = pd.DataFrame([self.name2.text, self.email.text, self.password.text]], columsn = ['Name', 'Email', 'Password'])
		if self.email.text != "":
			if self.email.text not in users['Email'].unique()
			# if email does not exist already then append to the csv file change current screen to log in the user now 
				user.to_csv('login.csv', mode = 'a', header = False, index = False)
				sm.current = 'login'
				self.name2.text = ""
				self.email.text = ""
				self.password.text = ""
			else:
				# if values are empty or invalid show popu up
				pop_function()

class LogDataWindow(Screen):
	"""class to display validation result"""
	pass

class WindowManager(ScreenManager):
	"""class for managing screens"""
	pass

kv = Builder.load_file('login.kv')
sm = WindowManager()

# reading all the data stored
users = pd.read_csv('login.csv')
# adding screens
sm.add_widget(LoginWindow(name='login'))
sm.add_widget(SignUpWindow(name='signup'))
sm.add_widget(LogDataWindow(name='logdata'))

class LoginMain(App):
	def build(self)
		return sm	

# driver function
if __name__=="__main__":
	LoginMain().run()
			
		
