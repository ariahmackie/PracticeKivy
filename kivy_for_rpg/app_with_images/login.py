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
from kivy.graphics import Rectangle, Color
from kivy.factory import Factory
Window.size = (400,800)
player1 = dp.create_test_user1()
player2 = dp.create_test_user2()
players = [player1, player2]


class Login(Screen):
    pass

class Home(Screen):
    pass

class ForgotPassword(Screen):
    pass

class PassCodeSubmission(Screen):
    pass

sm = ScreenManager(transition = NoTransition())
sm.add_widget(Login(name='login'))
sm.add_widget(Home(name='home'))

class LoginApp(MDApp):
    def build(self):
        self.sm = ScreenManager(transition = NoTransition())
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(Home(name='home'))
        self.sm.add_widget(ForgotPassword(name = 'forgotpassword'))
        self.sm.add_widget(PassCodeSubmission(name = 'passcodesubmission'))
        return self.sm

    def read_login_input(self,email, password):
        self.validate_password(email, password)

    def validate_password(self, email, password):
        player = lh.get_registered_player_via_email(email, players)
        if player != 0:
            print(player)
            if lh.is_correctpassword(player, password):
                self.sm.current = "home"
            else:
                print("incorrect password")
                self.password_error_message()
        else:
            print("alert. Is not registered email.")

    def password_error_message(self):
        warning = Label(text = '[color=ff3333]Wrong password.[/color]', markup = True, pos = (270, 270), size = (50, 50), size_hint = (None, None)  )
        self.sm.current_screen.add_widget(warning)

    def forgotpassword(self):
        self.sm.current = 'forgotpassword'

    def passcodesubmission(self, email):
        player = lh.get_registered_player_via_email(email, players)
        if player != 0:
            print("trying to send passcode")
            self.sm.current = 'passcodesubmission'
            self.correct_passcode = lh.email_passcode(email)
            print(self.correct_passcode)

    def validate_passcode(self,user_passcode):
        if str(user_passcode) == str(self.correct_passcode):
            self.sm.current = 'home'
            Factory.ChangePasswordPopup().open()

        else:
            warning = Label(text = '[color=ff3333]Wrong passcode.[/color]', markup = True, pos = (270, 370), size = (50, 50), size_hint = (None, None))
            self.sm.current_screen.add_widget(warning)



if __name__ == "__main__":
    LoginApp().run()
