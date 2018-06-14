from PyQt5.QtCore import QDate

xmas1 = QDate(2016, 12, 24)
xmas2 = QDate(2018, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last Christmas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next Christmas".format(nofdays))
