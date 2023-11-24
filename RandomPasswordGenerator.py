import os
import random
import string
from termcolor import colored

LINE = '-' * 55
MAX_LENGHT_NUMBER = 20
MIN_LENGHT_NUMBER = 4

settings = {
    'upper_case': True,
    'lower_case': True,
    'symbol_case': True,
    'number': True,
    'space': False,
    'lenght': 8
}

def clear_screen():
    os.system('cls')


def welcome_message():
    clear_screen()
    print()
    print(colored(LINE , 'blue' , attrs=['bold']) , end= ' ')
    print(colored('<<< W E L C O M E  T O  T H E  R A N D O M  P A S S W O R D  G E N E R A T O R >>>' , 'green' , attrs=['bold']) , end=' ')
    print(colored(LINE , 'blue' , attrs=['bold']))
    print('\n')
    print(colored('Defult settings for your random password is: (Uppercase , Lowercase , Symbolcase , Number / and with lenght = 8)' , 'magenta'))
    print()


def get_yes_or_no_for_setting_options(option , defult):
    while True:
        print()
        user_input = input(f'Include {option} in your password? (y/n): ')
        if user_input.lower() in ['y' , 'n']:
            if user_input.lower() == 'y':
                return True
            return False            
        else:
            print()
            print(colored('Invalid input. Please enter: y = (Yes) or n = (No)' , 'red'))           
            print(colored('Please try again.' , 'red'))
            print(LINE)


def get_lenght_of_the_password(max_lenght = MAX_LENGHT_NUMBER , min_lenght = MIN_LENGHT_NUMBER):
    while True:
        print()
        user_input = input('Enter lenght of your password: ')
        if user_input.isdigit() and min_lenght <= int(user_input) <= max_lenght:
            return int(user_input)
        else:
            print()
            print(colored('Invalid input. Please enter "positive number" between 4 and 20 .' , 'red'))
            print(LINE)


def setting_of_the_password(settings):
    for (option , defult) in settings.items():
        if option != 'lenght':
            settings[option] = get_yes_or_no_for_setting_options(option , defult) #choon dar tabe return shode pas meghdar dehi mishe.
        else:
            settings[option] = get_lenght_of_the_password() #choon dar tabe return shode pas meghdar dehi mishe.
    
    password_generator(settings)
            

def do_you_want_change_defult_options_setting():
    while True:
        user_input = input('Do you want change defult options setting? (y/n): ')
        if user_input.lower() in ['y' , 'n']:
            if user_input.lower() == 'y':
                print()
                setting_of_the_password(settings)
                return
            else:
                print()
                password_generator(settings)
                return
        else:
            print()
            print(colored('Invalid input. Please enter y = (Yes) , n = (No)' , 'red'))
            print(LINE)
            

def upper_case_chars():
    return random.choice(string.ascii_uppercase)

def lower_case_chars():
    return random.choice(string.ascii_lowercase)

def symbol_case_chars():
    return random.choice(string.punctuation)

def number_for_password():
    return random.choice(string.digits)


def select_random_password(choices):

    choice = random.choice(choices)

    if choice == 'upper_case':
        return upper_case_chars()
    if choice == 'lower_case':
        return lower_case_chars()
    if choice == 'symbol_case':
        return symbol_case_chars()
    if choice == 'number':
        return number_for_password()
    if choice == 'space':
        return ' '
 

def password_generator(settings):
    password_generated = ''
    lenght = settings['lenght']

    choices = []

    for option , defult in settings.items():
        if defult == True:
            choices.append(option)

    #choices = list(filter(lambda x: settings[x] , ['upper_case' , 'lower_case' , 'symbol_case' , 'number' , 'space']))

    for i in range(lenght):
        password_generated += select_random_password(choices) 
    print()
    print(colored(f'Your password is: {password_generated}' , 'green' , attrs=['bold']))
    print()


def do_you_want_another_password():
    while True:
        user_input = input('Do you want another password? (y/n): ')
        if user_input.lower() in ['y' , 'n']:
            if user_input.lower() == 'y':
                print(LINE)
                do_you_want_change_defult_options_setting()
            else:   
                print('\n')
                print(colored('<<< END OF THE PROGRAMM >>>' , 'green' , attrs=['bold']))
                print(colored('<<< THANK YOU FOR CHOOSING US >>>' , 'white' , attrs=['bold']))
                print(colored('<<< GOOD LUCK >>>' , 'red' , attrs=['bold']))
                return
        else:
            print()
            print(colored('Invalid input. Please enter y = (Yes) or n = (No)' , 'red'))
            print(LINE)


def run():
    clear_screen()
    welcome_message()
    do_you_want_change_defult_options_setting()
    do_you_want_another_password()

if __name__ == "__main__":
    run()
