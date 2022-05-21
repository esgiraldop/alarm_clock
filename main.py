import datetime
from dateutil.parser import parse
import pytz
import beep

bog_timezone = pytz.timezone('America/Bogota')
alarm_time = '21:43:30'
alarm_time_parsed = parse(alarm_time)
# Have to use the following in order for the times to work
    # See --> https://towardsdatascience.com/basic-datetime-operations-in-python-2d706be82c63
alarm_time_parsed_loc = bog_timezone.localize(alarm_time_parsed)
default_tzinfo = (datetime.timedelta(days=-1, seconds=68640), datetime.timedelta(0), 'LMT')

while True:
    now = datetime.datetime.now()
    now_loc = bog_timezone.localize(now)
    if now > alarm_time_parsed:
        beep.nine_beeps()
        break