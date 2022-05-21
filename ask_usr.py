from datetime import *
import re

def main_menu():
    ans = '0'
    while ans not in ['1', '2']:
        print('Please choose an option. Do you want to:')
        print('1. Set the alarm to sound within a certain period of time (Temporizer).')
        ans = input('2. Set the alarm to sound at given date and time: ')

        if ans not in ['1', '2']:
            print('Please enter a valid answer.')

    return ans

def ask_minutes():
    # Check whether the input is a number
    # Check whether the number is between 1 and 5 (minutes)
    pass

def ask_datetime():
    # Check the correct format is entered (With re maybe?)
    # Check whether the datetime is later than the current time
    now = now
    pass

if __name__ == '__main__':
    ans = main_menu()
    print('Your answer is: ', ans)