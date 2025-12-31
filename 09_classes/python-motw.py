"""
9-15. Python Module of the Week: 

One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
http://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, or explore the documentation of
the collections and random modules.
"""

import calendar
import sys

# c = calendar.TextCalendar(calendar.MONDAY)
# c.prmonth(2025, 10)

# print(c.formatyear(2025, 2, 1, 1, 3))

if len(sys.argv) > 1:
    year = int(sys.argv[1])
else:
    year = 2025  # Default year if no argument is provided

for month in range(1, 13):

    c = calendar.monthcalendar(year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('{:>3}: {:>2}'.format(calendar.month_abbr[month], meeting_date))
