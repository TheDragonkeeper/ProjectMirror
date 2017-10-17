import json
from datetime import datetime, timedelta
import time
from icalendar import Calendar, Event, vDatetime
import sys  
sys.path.append('..')
import mirrorproject

def getTodayEvents(ics):
    ics_file = open(ics, 'r').read()
    cal = Calendar.from_ical(ics_file)

    today = datetime.today().date()
    day2 = today+timedelta(days=1)
    day3 = today+timedelta(days=2)
    day4 = today+timedelta(days=3)
    day5 = today+timedelta(days=4)
    calendarentries = []
    for event in cal.walk('VEVENT'):
        dtstart = event['DTSTART'].dt
        summary = event['SUMMARY']
        dtend = event['DTEND'].dt
#        print(dtstart + ' ' + summary)
        if dtend <= dtstart+timedelta(days=1):
            if dtstart <= today <= dtend:
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day2 <= dtend:
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day3 <= dtend:
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day4 <= dtend:
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day5 <= dtend:
                calendarentries.append(str(dtstart) + ' ' + summary)
        else:
            if dtstart <= today <= dtend:
                dtstart = today
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day2 <= dtend:
                dtstart = day2
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day3 <= dtend:
                dtstart = day3
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day4 <= dtend:
                dtstart = day4
                calendarentries.append(str(dtstart) + ' ' + summary)
            if dtstart <= day5 <= dtend:
                dtstart = day5
                calendarentries.append(str(dtstart) + ' ' + summary)
    calendarentries.sort()
    for x in calendarentries:
          mirrorproject.iCALlreturn(x)

