from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from Model.helpers import login_helper as lh
from Model.helpers import dummy_players as dp

Window.size = (400,800)
player1 = dp.create_test_user1()
player2 = dp.create_test_user2()
players = [player1, player2]


class Login(Screen):
    pass

class Home(Screen):
    pass
sm = ScreenManager(transition = NoTransition())
sm.add_widget(Login(name='login'))
sm.add_widget(Home(name='home'))
class LoginApp(MDApp):
    def build(self):
        self.sm = ScreenManager(transition = NoTransition())
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(Home(name='home'))
        return self.sm

    def read_login_input(self,email, password):
        print("submitted log in")
        print(email)
        print(password)
        self.validate_password(email, password)

    def validate_password(self, email, password):
        player = lh.get_registered_player_via_email(email, players)
        if player != 0:
            print(player)
            if lh.is_correctpassword(player, password):
                self.sm.current = "home"
            else:
                print("incorrect password")
                warning = Label(text = '[color=ff3333]Wrong password.[/color]', markup = True )
                self.sm.current_screen.add_widget(warning)
        else:
            print("alert. Is not registered email.")


        # sm.current = "home"

if __name__ == "__main__":
    LoginApp().run()