import datetime
from dateutil.parser import parse
import pytz
import beep

bog_timezone = pytz.timezone('America/Bogota')
alarm_time = '23:11'
alarm_time_parsed = parse(alarm_time)
alarm_time_parsed = alarm_time_parsed.replace(tzinfo=bog_timezone)

while True:
    now = datetime.datetime.now(tz=bog_timezone)
    if now > alarm_time_parsed:
        beep.nine_beeps()
        break
