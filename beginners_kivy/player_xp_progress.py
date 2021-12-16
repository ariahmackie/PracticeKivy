from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from player import Player
from player import Task
import dummy_players
import datetime

player1 = dummy_players.create_test_user1()
Builder.load_file('xp_progress.kv')

classimport datetime Progress_Bar(Widget):
    def complete_task(self):
        task = Task("run a mile", datetime.date.today(), 2, False)
        player1.add_to_experience(task)
        self.ids.xp_progress_bar.value = player1.experience
        self.ids.xp_label.text = f'{int(player1.experience)} % Progress'

class AwesomeApp(App):
    def build(self):
        return Progress_Bar()

if __name__ == '__main__':
    AwesomeApp().run()
