import calendar
#Create a plain text calendar
c= calendar.TextCalendar(calendar.THURSDAY)
str= c.formatmonth(2017,10,1,0)
print str
