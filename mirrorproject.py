
from tkinter import *
import time
from datetime import datetime, timedelta
from icalendar import Calendar, Event
import calendar
import forecastio

root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
mainfont = 'mono'
bgcolour = 'black'
fgcolour = 'white'


##### gui 
#clock
clock = Label(root, font=(mainfont, 50, 'bold'), bg=bgcolour, fg=fgcolour)
clock.pack(fill=BOTH, expand=1)
clock.place(x=10,y=0)
#calender
calenderl = Label(root, font=(mainfont, 16, 'bold'), bg=bgcolour, fg=fgcolour, justify=LEFT)
calenderl.pack(fill=BOTH, expand=0, side=LEFT, anchor='w')
calenderl.place(x=30,y=80)
#date
currentdatel = Label(root,  font=(mainfont, 25, 'bold'), bg=bgcolour, fg=fgcolour, justify=LEFT)
currentdatel.pack(fill=BOTH, expand=0, side=LEFT, anchor='w')
currentdatel.place(x=15,y=280)
#calender.events
ics = "/home/dragon/USHolidays.ics"
iCALl = Label(root, font=(mainfont, 16, 'bold'), bg=bgcolour, fg=fgcolour, justify=LEFT)
iCALl.pack(fill=BOTH, expand=0, side=LEFT, anchor='w')
iCALl.place(x=15,y=350)
#forcast
api_key = "d65a033e1b1486e87eb450cf04dbc992"
lat = -31.967819
lng = 115.87718
forecastl = Label(root,  font=(mainfont, 25, 'bold'), bg=bgcolour, fg=fgcolour, justify=RIGHT)
forecastl.pack(fill=BOTH, expand=0, side=RIGHT, anchor='e')
forecastl.place(x=1000,y=20)


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
time1 = ''
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
    calyear = datetime.today().year
    calmonth  = datetime.today().month
    calb4 = cal.formatmonth(calyear,calmonth)
    calb44 = calb4.replace(str(calyear), '')
    namemonth = datetime.now().strftime("%B")
    caldisp = str(str(calb44.replace(namemonth, '')))
    calenderl.config(text=caldisp)
    calenderl.after(20000, calenderf) ##change this to update when date changes
	
def currentdatef():
    year = datetime.today().year
    month  = datetime.now().strftime("%B")
    day = datetime.today().day
    currentdatel.config(text=str(str(day) + ' ' + str(month) + ' ' + str(year)))
    currentdatel.after(20000, currentdatef)

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
    z = print('\n')
    for y in calendarentries:
        x = y + str(z)
        iCALl.config(text=x)
        
def forecast():
	today = datetime.today().date()
	day2 = today+timedelta(days=1)
	day3 = today+timedelta(days=2)
	day4 = today+timedelta(days=3)
	day5 = today+timedelta(days=4)
	forecast = forecastio.load_forecast(api_key, lat, lng)
	byHour = forecast.currently()
	print(str(byHour.temperature) + ' ' + str(byHour.icon) + ' ' + str(byHour.summary))

getTodayEvents(ics)
forecast()
calenderf()
currentdatef()
tick()
root.mainloop()
