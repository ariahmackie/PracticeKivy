import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.label import Label #uix module has layouts and widgets
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs) # call super to implement the base Gridlayout, always call super with **kwargs

		self.cols = 2

		self.add_widget(Label(text='username'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)


		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)




class MyApp(App): # my base class inherits from App. The only part i change is "MyApp"
	def build(self): #this method initializes and returns root widget
		return LoginScreen()


if __name__ == '__main__':
	MyApp().run()  #always run kivy app with BaseClass().run()
