from datetime import *
import pytz
from dateutil.parser import parse

def main_menu():
    ans = '0'
    while ans not in ['1', '2']:
        print('Please choose an option. Do you want to:')
        print('1. Set the alarm to sound within a certain period of time (Temporizer).')
        ans = input('2. Set the alarm to sound at a given date and time: ')

        if ans not in ['1', '2']:
            print('Please enter a valid answer.')

    return ans

def ask_minutes():
    print('------TEMPORIZER------')
    while True:
        ans = input('Please input the time (Integer number, between 0 and 5 minutes): ')

        try:
            ans = int(ans)
        except:
            print('Enter a valid answer')
            continue
        else:
            if ans < 0 or ans > 5:
                print('Enter a number between 0 and 5')
                continue

        break

    return ans

def ask_timezone():

    def display_timezones():
        ans2 = 's'
        while ans2 not in ['y', 'n']:
            ans2 = input('Do you want to see the list of available timezones? (y/n): ').lower()

            if ans2 not in ['y', 'n']:
                print('Please select a valid answer')

        if ans1 == 'y':
            print('The supported timezones are:')
            print(*pytz.all_timezones, sep='\n')
            print('\n')

    print('First, you have to select your timezone. The default timezone is "America/Bogota".')
    ans1 = 's'
    while ans1 not in ['y', 'n']:
        ans1 = input('Do you want to change the timezome? (y/n): ').lower()

        if ans1 not in ['y', 'n']:
            print('Please select a valid answer')

    if ans1 == 'y':
        display_timezones()

        tzone = 's'
        while tzone not in pytz.all_timezones:
            tzone = input('Please enter the timezone: ')
            if tzone not in pytz.all_timezones:
                print('Please enter a valid zone')
                display_timezones()

    else:
        tzone = 'America/Bogota'

    return tzone

def ask_datetime():
    print('------ALARM------')
    timezone = ask_timezone()  # Default timezone is 'America/Bogota'
    timezone = pytz.timezone(timezone)
    print('\nNext, please select the time')
    print('Supported formats for the time: "hh:mm" or "h:mm" (Military time)')
    # For practicity, only hours and minutes are allowed. This hours and minutes are parsed as being in the same day
    while True:
        ans = input('Please input the time: ')

        if (len(ans) < 4 or len(ans) > 5) or ':' not in ans:
            print('Enter a valid time')
            continue

        hour, _, minute = ans.partition(':')
        if (len(hour) < 1 or len(hour) > 2) or (len(minute) < 1 or len(minute) > 2):
            print('Formats other than "hh:mm" or "h:mm" are not accepted.')
            continue
        elif len(hour) == 2 and len(minute) == 1:   # For rejecting format "hh:m"
            print('Format "hh:m" not allowed. Enter the time in the correct format ("hh:mm", "h:mm").')
            continue

        try:
            hour = int(hour)
            minute = int(minute)
        except:
            print('Enter only integer numbers for the time.')
            continue
        else:
            if hour < 0 or hour > 23:
                print('Only numbers between 0 and 23 can be entered for the hours')
            elif minute < 0 or minute > 59:
                print('Only numbers between 0 and 59 can be entered for the minutes')
            else:
                # Time to check the time given by the user is not 'lesser' than the current time
                now = datetime.now() # Current time
                now_loc = timezone.localize(now)
                usr_time = str(hour)+':'+str(minute)
                usr_time = parse(usr_time)
                usr_time_loc = timezone.localize(usr_time)
                if usr_time_loc < now_loc:
                    print('The entered time must be "greater" the the current time.')
                    continue

                break # The time is well formatted

    return usr_time_loc, now_loc, timezone


if __name__ == '__main__':
    # ans = ask_datetime()
    # print('The datetime set for your alarm is: ', ans)
    ans = ask_minutes()
    print('Your minutes are: ',  ans)