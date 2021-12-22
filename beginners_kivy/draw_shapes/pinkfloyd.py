#recreating the dark side of the moon albumn (without gradient fade)

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout



class AlbumLayout(RelativeLayout):
	pass



class AlbumCover(App):
	def build(self):
		return AlbumLayout()

if __name__ == "__main__":
	cover = AlbumCover()
	cover.run()
