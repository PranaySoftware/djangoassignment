"""
Create a method which returns interval date by the following condition
Give start and end date (both inclusive) in the ‘YYYYMMDD’ format (ex. 20181231 is 31st Dec 2018), output list of dates that satisfy exactly one of the following conditions. The output should be in chronological order. One date per line. Input dates belong between the year 1900 to 2100.
1. The day is the 4th Saturday of the month.
2. The day is Saturday and the date is multiple of 5.
"""

import datetime
import math 

class InvalidDate(Exception):
    """Invalid Date \
    Year should be within 1900 to 2100 \
    Startdate should be less than End Date"""
    pass

def validDate(tdate):
    try:
        tdate = datetime.datetime.strptime(tdate, '%Y%m%d')
        year = tdate.strftime("%Y")
        if int(year) >= 1900 and int(year)<=2100:
            return True
        else:
            raise InvalidDate
    except:
        raise InvalidDate

def is4thstrday(tdate):
    return math.ceil(int(tdate.strftime("%d"))/7) == 4

def ismultipleby5(tdate):
   return int(tdate.strftime("%d"))%5 == 0

def allsaturday(startdate, enddate):
    if validDate(startdate) and validDate(enddate):
        startdate = datetime.datetime.strptime(startdate,'%Y%m%d')
        enddate = datetime.datetime.strptime(enddate,'%Y%m%d')
        if enddate > startdate:
            datearr = []
            startstrday = startdate + datetime.timedelta(6-int(startdate.strftime("%w")))
            while startstrday < enddate:
                if bool(is4thstrday(startstrday)) != bool(ismultipleby5(startstrday)):
                    datearr.append(startstrday.strftime("%Y%m%d"))
                startstrday = startstrday + datetime.timedelta(7)
            return datearr
        else:
            raise InvalidDate
    else:
        raise InvalidDate

if __name__ == '__main__':
    print("Enter Start date with format as : YYYYMMDD")
    startdate = str(input())
    print("Enter End date with format as : YYYYMMDD")
    enddate = str(input())
    result = allsaturday(startdate, enddate)
    for tdate in result:
        print(tdate)
            







