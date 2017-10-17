from tkinter import * # gui
import sys  
sys.path.append('modules')  
import time # clock
import calendar
import datetime
from subprocess import call

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
import ical
iCALl = Label(root, font=(mainfont, 16, 'bold'), bg=bgcolour, fg=fgcolour, justify=LEFT)
iCALl.pack(fill=BOTH, expand=0, side=LEFT, anchor='w')
iCALl.place(x=30,y=130)

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
    calyear = datetime.datetime.today().year
    calmonth  = datetime.datetime.today().month
    calb4 = cal.formatmonth(calyear,calmonth)
    calb44 = calb4.replace(str(calyear), '')
    namemonth = datetime.datetime.now().strftime("%B")
    caldisp = str(str(calb44.replace(namemonth, '')))
    calenderl.config(text=caldisp)
    calenderl.after(20000, calenderf) ##change this to update when date changes

def currentdatef():
    year = datetime.datetime.today().year
    month  = datetime.datetime.now().strftime("%B")
    day = datetime.datetime.today().day
    currentdatel.config(text=str(str(day) + ' ' + str(month) + ' ' + str(year)))
    currentdatel.after(20000, currentdatef)


ics = "/home/dragon/USHolidays.ics"
ical.getTodayEvents(ics)
calenderf()
currentdatef()
tick()
root.mainloop()
