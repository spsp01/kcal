import datetime

def dni():
    dt = datetime.datetime(2010, 12, 1, 8,)
    end = datetime.datetime(2010, 12, 1, 16, 29, 59)
    step = datetime.timedelta(minutes=30)

    result = []
    #counter = 1
    while dt < end:
        result.append((dt.strftime('%H:%M')))
        dt += step

    return(result)