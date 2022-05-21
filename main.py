import datetime
from dateutil.parser import parse
import pytz
import beep
import ask_usr

bog_timezone = pytz.timezone('America/Bogota')

ans = ask_usr.main_menu()
if ans == 1:
    ans = ask_usr.ask_minutes()
    now = datetime.datetime.now()
    now = bog_timezone.localize(now)
    deltatime = datetime.timedelta(minutes=ans)
    alarm_time = now + deltatime
else:
    ans = ask_usr.ask_datetime()
    alarm_time = '21:43:30'
    alarm_time = parse(alarm_time)

# Have to use the following in order for the times to work
    # See --> https://towardsdatascience.com/basic-datetime-operations-in-python-2d706be82c63
alarm_time = bog_timezone.localize(alarm_time)
default_tzinfo = (datetime.timedelta(days=-1, seconds=68640), datetime.timedelta(0), 'LMT')

while True:
    now = datetime.datetime.now()
    now = bog_timezone.localize(now)
    if now > alarm_time:
        beep.nine_beeps()
        break