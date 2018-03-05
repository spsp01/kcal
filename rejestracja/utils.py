import datetime

def godziny():
    dt = datetime.datetime(2010, 12, 1, 8,)
    end = datetime.datetime(2010, 12, 1, 18, 29, 59)
    step = datetime.timedelta(minutes=30)

    result = []
    #counter = 1
    while dt < end:
        result.append((dt.strftime('%H:%M')))
        dt += step

    return(result)

def is_alpha(s):
    if s.isalpha():
       return True
    return False


