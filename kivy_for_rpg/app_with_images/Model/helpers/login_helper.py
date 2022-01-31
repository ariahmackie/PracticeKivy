import string
import re
import random
from Model.email import Email

def get_registered_player_via_username(username, players): #createaccount_login_forgot_password helpers
    for player in players:
        if player.player_account.username == username:
            return player
    return 0

def get_registered_player_via_email(email, players): #createaccount_login_forgot_password helpers
    for player in players:
        if player.player_account.email == email:
            return player
        return 0

def is_correctpassword(CURRENT_PLAYER, password): #createaccount_login_forgot_password helpers
    if CURRENT_PLAYER.player_account.password == password:
        return True
    else:
        return False

def email_passcode_1(players): #createaccount_login_forgot_password helpers
    receiver_address = str(raw_input("Please type your email >"))
    player = get_registered_player_via_email(receiver_address, players)
    if player != 0:
        global CURRENT_PLAYER
        CURRENT_PLAYER = player
        passcode = generate_five_digit_passcode()
        newemail = Email(receiver_address, "Passcode", str(passcode))
        newemail.send()
        user_submit_code(passcode)
    else:
        print("Sorry. That email doesn't exist in the database")

def email_passcode(email):
    receiver_address = email
    passcode = generate_five_digit_passcode()
    newemail = Email(receiver_address, "Passcode", str(passcode))
    newemail.send()
    return passcode

def generate_five_digit_passcode(): #createaccount_login_forgot_password helpers
    passcode = random.randint(00000, 99999)
    return passcode

def user_submit_code(generatedpasscode): #createaccount_login_forgot_password helpers
    """user places their code, confirm if it is correct"""
    user_passcode = int(raw_input("Please type 5 digit passcode. >"))
    if generatedpasscode == user_passcode:
        welcome_menu()
    else:
        print("incorrect passcode")


def get_validemail(players):#createaccount_login_forgot_password helpers
    email = str(raw_input("please write an email. >"))
    email_form = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(email_form, email):
        player = get_registered_player_via_email(email)
        print(player)
        if player == 0:
            return email
        else:
            print("User email already exists. Please login.")
            login_menu()
    else:
        print("Not a valid email. ")
        get_validemail()

def get_validusername(): #createaccount_login_forgot_password helpers
    username = str(raw_input("Please write a username. >"))
    if username == "":
        print("Invalid Username. Can't be empty")
        get_validusername()
    else:
        return username


def get_validpassword(): #createaccount_login_forgot_password helpers
    """ check if password has a length >= 7 characters,
     has one of the special characters !@#$%*, has letters, and numbers - if it doesn't pass reprompt create_account"""
    password = str(raw_input("Please type a password. Requirements: \nat least 7 characters.\nat least one letter and number.\nMust use one of the following characters:!@#$%*  >"))
    char_options = ["!", "@", "#", "$", "%", "*"]
    num_options = list(string.digits)
    letter_options = list(string.ascii_letters)
    no_special_characters = does_not_have_value(char_options, password)
    no_numbers = does_not_have_value(num_options, password)
    no_letters = does_not_have_value(letter_options, password)
    if len(password) < 7:
        print("Password too short")
        get_validpassword()
    elif no_special_characters:
        print("Need to use at least one: !@#$%*")
        get_validpassword()
    elif no_numbers:
        print("Need to include a number")
        get_validpassword()
    elif no_letters:
        print("need to include letters")
        get_validpassword()
    else:
        return password

def does_not_have_value(substring_list, word): #createaccount_login_forgot_password helpers
    for substring in substring_list:
        if substring in word:
            return False
    return True
