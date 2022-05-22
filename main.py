import datetime
import time
import pytz
import beep
import ask_usr

ans = ask_usr.main_menu()
if ans == '1': # Temporizer
    minutes = ask_usr.ask_minutes()
    now = datetime.datetime.now()

    # Have to use the following in order for the times to work
    # See --> https://towardsdatascience.com/basic-datetime-operations-in-python-2d706be82c63
    timezone = pytz.timezone('America/Bogota') # For this case, it does not matter the timezone
    now = timezone.localize(now)

    #Adding the minutes entered by the user to the current time
    deltatime = datetime.timedelta(minutes=minutes)
    alarm_time = now + deltatime
else: # alarm
    alarm_time, now, timezone = ask_usr.ask_datetime()

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    now = timezone.localize(now)
    if now > alarm_time:
        beep.nine_beeps()
        print('**************************')
        print('¡¡¡¡¡¡¡¡¡¡ BEEP !!!!!!!!!!')
        print('**************************')
        break

    print('---------------------------')
    print('The current time is: ', now.time().strftime('%H:%M:%S'))
    print('The alarm time is: ', alarm_time.time().strftime('%H:%M:%S'))
    print('---------------------------')
    print('\n')