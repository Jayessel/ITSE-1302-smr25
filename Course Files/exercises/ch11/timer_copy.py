#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time.strftime('%I:%M:%S %p'))
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print("Stop time: ", stop_time.strftime('%I:%M:%S %p'))
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if minutes > 0:
        print(f'Hours/minutes: {hours:02}:{minutes:02}')
    if days > 0:
        print("Days:", days)
    print(f"Seconds: {time_object.second}.{time_object.microsecond}")

if __name__ == "__main__":
    main()
