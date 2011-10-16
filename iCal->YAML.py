from icalendar import Calendar, Event
from datetime import datetime
import csv, re, time

cal = Calendar.from_string(open('events_rss.ics','rb').read())
filename = 'output.csv'
starthour = []
with open(filename, 'wt') as f:
   writer = csv.writer(f)
   writer.writerow(('summary','address', 'dtstart','dtend','lat','long'))

   for i, component in enumerate(cal.walk()):
     if component.name == 'VEVENT':
       summary = component.get('summary')
       desc = component.get('description')
       tstart = str(component.get('dtstart'))
       tend = component.get('dtend')
       
       m = re.search('(([0-1]?[0-9])|([2][0-3])):([0-5]?[0-9])(:([0-5]?[0-9]))?',str(desc))
       
       if m:
         firsttime = str(m.group(0))
       else:
         firstime = 'none'
       if firsttime:
         # start.append(m.group(0))
         h = re.search('([0-1]?[0-9])|([2][0-3]):?',firsttime)
         if h:
           temp = h.group(0)
         else:
           None
       else:
         print 'na'
        # start.append('none')
       start_time_tuple = datetime(int(tstart[0:4]),int(tstart[4:6]),int(tstart[6:8]),int(temp),0,0)
       print start_time_tuple

       writer.writerow((summary, desc, start_time_tuple, tend, 'na', 'na'))
      
      

    #tstart/tend 2011-11-09-T080000Z
