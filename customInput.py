def inputFormatted():
    x = input()
    print()
    return x

def inputDateTime(dateInputString = "Enter days of week, seperated by a comma if needed (1(Monday)-7(Sunday)):\n", timesInputString = "Enter start and end times in the format \"start-end\", seperated by a comma if needed (0-23)\n"):
    datetimes = {}

    days = list(map(int, input(dateInputString).split(",")))

    for day in days:
        times = input(timesInputString).split(",")
        
        for i in range(len(times)):
            times[i] = times[i].split("-")
            times[i] = (int(times[i][0]), int(times[i][1]))
        
        datetimes[day] = times
    
    return datetimes