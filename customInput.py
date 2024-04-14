def inputFormatted():
    x = input()
    print()
    return x

def inputDateTime(dateInputString = "Enter days of week, seperated by a comma if needed (1(Monday)-7(Sunday)):\n", timesInputString = "Enter start and end times in the format \"start-end\", seperated by a comma if needed (0-23)\n"):
    datetimes = {}

    try:
        days = list(map(int, input(dateInputString).split(",")))
    except:
        print("Invalid input. Please try again.")
        return inputDateTime(dateInputString, timesInputString)

    for day in days:
        if(day < 1 or day > 7):
            print("Invalid day entered, will be skipped.")
            continue
        
        times = input(timesInputString).split(",")
        
        for i in range(len(times)):
            times[i] = times[i].split("-")

            try:
                times[i] = (int(times[i][0]), int(times[i][1]))
            except:
                print("Invalid time entered, will be skipped.")
                del times[i]
        
        datetimes[day] = times
    
    return datetimes