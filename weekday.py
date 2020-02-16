#John Paul Lee
#Programming and Scripting Week 5 Homework

#import datetime to calaulate the date
import datetime

#have now = todats date
now = datetime.datetime.now()

#have n = what day of the week it is
n = datetime.datetime.today().weekday()

#if it is a weekday print Yes, unfortunately today is a weekday
if n <= 4:
    print("Yes, unfortunately today is a weekday")

#if it is the weekend print It is the weekend, yay!
else:
    print("It is the weekend, yay!")

