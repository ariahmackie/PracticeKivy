#recreating the dark side of the moon albumn (without gradient fade)

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout



class AlbumnLayout(RelativeLayout):
	pass



class AlbumnCover(App):
	def build(self):
		return AlbumnLayout()

if __name__ == "__main__":
	cover = AlbumnCover()
	cover.run()
