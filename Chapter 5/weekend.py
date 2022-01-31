import datetime
# weekdays tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week which is an intefer
dayOfWeek=now.weekday()
# subscript into weekDays using the dayOfWeek
today=weekDays[dayOfWeek]
#calculate and print days until the weekend
daysToWeekend=6-dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend")
#flag to only print 1 quote in for loop
quotePrinted="false"
#prints week days left until weekend with a quote
for left in weekDays[dayOfWeek:6]:
    if today=="Sundday" and quotePrinted=="false":
        print(left, " Sunday is Homework marathon day!")
        quotePrinted="true"
    elif(today=="Monday" or today=="Tuesday" or today=="Wednesday") and quotePrinted=="false":
        print(left, "When is Friday? I feel like it should be Friday already...")
        quotePrinted="true"
    elif today=="Thurdsay" and quotePrinted=="false":
        print(left,"This week is taking forever!")
        quotePrinted="true"
    elif quotePrinted=="false":
        print(left,"Finally..")
        quotePrinted="true"
    else:
        print(left)
        