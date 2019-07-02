# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    _next_day = (year, month, day+1)
    if day == 30:
        _next_day = (year, month+1, 1) if month < 12 else (year+1, 1, 1)        
    return _next_day
      
def dateIsBefore(year1, month1, day1, year2, month2, day2): 
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2 and day1 < day2:
            return True
        else:
            return False
    return False
        
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        date1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

print("Holas 4")
print(daysBetweenDates(2012,9,30,2012,10,30))