import kivy
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
	def build(self):
		btn = Button(text="Press me", size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y' : .5})
		btn.bind(on_press=self.on_press_button)
		return btn

	def on_press_button(self, instance):
		print("you pressed the button")


if __name__=='__main__':
	app = MainApp()
	app.run()
