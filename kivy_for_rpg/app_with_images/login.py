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
from Model.player import Player
from Model.helpers import dummy_players as dp
from kivy.graphics import Rectangle, Color
from kivy.factory import Factory
from kivy.uix.dropdown import DropDown
import re

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

class NewAccount(Screen):
    pass

class NewTask(Screen):
    def build(self):
        dropdown = DifficultyDropDown()
        mainbutton = Button(text = "z", size_hint = (None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(onselect=lambda instance, x: setattr(mainbutton, 'text', x))
    # def build(self):
    #     self.dropdown = DropDown()
    #
    #     self.easy_button = Button(text = "easy", size_hint_y = None, height = 40)
    #     self.easy_button.bind(on_release= lambda self.easy_button: self.dropdown.select(self.easy_button.text))
    #
    #     self.medium_button = Button(text = "medium", size_hint_y = None, height = 40)
    #     self.medium_button.bind(on_release= lambda self.medium_button: self.dropdown.select(self.medium_button.text))
    #
    #     self.hard_button = Button(text = "hard", size_hint_y = None, height = 40)
    #     self.hard_button.bind(on_release = lambda self.hard_button: self.dropdown.select(self.hard_button.text))
    #
    # ass    self.dropdown.add_widget(self.easy_button)
    #     self.dropdown.add_widget(self.medium_button)
    #     self.dropdown.add_widget(self.hard_button)
    #
    #     self.main_button = Button(text = "Select Difficulty", size_hint = (None, None))
    #     self.main_button.bind(on_release = self.dropdown.open)
class DifficultyDropDown(DropDown):
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
        self.sm.add_widget(NewAccount(name = 'newaccount'))
        self.sm.add_widget(NewTask(name = 'newtask'))
        return self.sm

    def to_new_account(self):
        self.sm.current = 'newaccount'

    def to_login(self):
        self.sm.current = 'login'

    def to_forgotpassword(self):
        self.sm.current = 'forgotpassword'

    def to_new_task(self):
        self.sm.current = 'newtask'
        NewTask().build()


    def create_new_user(self, username, email, password):
        if self.is_valid_account(username, email, password):
            new_player = Player(email, username, password)
            self.player = new_player
            self.sm.current = "home"
        else:
            print("Did not make an account.")

    def is_valid_account(self, username, email, password):
        if self.is_available_username(username):
            if self.is_available_email(email):
                #if self.is_valid_email(email):
                #    return True
                return True
        else:
            return False

    def is_available_username(self, username):
        player = lh.get_registered_player_via_username(username, players)
        if player == 0:
            return True
        print("username not available")
        return False

    def is_available_email(self, email):
        player = lh.get_registered_player_via_email(email, players)
        if player == 0:
            return True
        print("email already used")
        return False

    def is_valid_email(self, email):
        rx =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # from https://www.geeksforgeeks.org/check-if-email-ress-valid-or-not-in-python/
        if re.fullmatch(rx, email):
            return True
        print("not a valid email")
        return False

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
        self.sm.current_screen._widget(warning)

    def forgotpassword(self):
        self.sm.current = 'forgotpassword'

    def passcodesubmission(self, email):
        self.player = lh.get_registered_player_via_email(email, players)
        if self.player != 0:
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
            self.sm.current_screen._widget(warning)

    def save_newpassword(self, newpassword):
        print("old password:")
        print(self.player.player_account.password)
        self.player.player_account.password = newpassword
        print("New password")
        print(self.player.player_account.password)

if __name__ == "__main__":
    LoginApp().run()
