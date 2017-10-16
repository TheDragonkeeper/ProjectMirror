from tkinter import * # gui
import time # clock
import calendar
import datetime
from subprocess import call

root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

time1 = ''
power = 1
clock = Label(root, font=('times', 50, 'bold'), bg='black', fg='white')
clock.pack(fill=BOTH, expand=1)
clock.place(x=0,y=0)
calenderl = Label(root, font=('times', 20, 'bold'), bg='black', fg='white')
calenderl.pack(fill=BOTH, expand=0)
calenderl.place(x=0,y=100)
def powerOFFtv():
    clock.config(text='Turning off TV')
    call(["tvservice", "-o"])

def powerONtv():
    call(["tvservice", "-p"])
    call(["fbset", "-depth", "16"])
    call(["xrefresh"])
    call(["fbset", "-depth", "32"])
    call(["xrefresh"])
    clock.config(text='Turning on TV')

def tick():
    global time1
    # get local time
    time2 = time.strftime('%H:%M:%S')
    # check time string for changes
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # update onscreen clock every 200 ms
    clock.after(200, tick)
    if time2 == "00:02:00":
        powerOFFtv()
    if time2 == "00:04:00":
        powerONtv()
    if time2 == "07:20:00":
        powerOFFtv()
    if time2 == "18:00:00":
        powerONtv()

def calenderf():
#Create a plain text calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calyear = datetime.datetime.today().year
    calmonth  = datetime.datetime.today().month
    caldisp = cal.formatmonth(calyear,calmonth)
    calenderl.config(text=caldisp)
    calenderl.after(200, calenderf)
"""
from datetime import datetime #calender
from icalendar import Calendar, Event, vDatetime #calender
import urllib3
import json

def calenderupdate():
    http = urllib3.PoolManager()
    calget = http.request('GET', 'www.calendarlabs.com/templates/ical/UK-Holidays.ics', preload_content=False)
    calget.release_conn()
    calgot = str(calget.data)
    cal = Calendar.from_ical(calgot)

    entries = []
    for event in cal.walk('VEVENT'):
        dtstart = event['DTSTART']
        dtend = event['DTEND']
        start = vDatetime.from_ical(dtstart)
        end = vDatetime.from_ical(dtend)
        if start <= today <= end:
            entry = {'summary' : event['SUMMARY'] }
            entries.append(entry)
    output = json.dumps(entries)


calenderupdate()
"""
calenderf()
tick()
root.mainloop()
