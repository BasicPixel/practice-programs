import time


def countdown(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = f"{mins:02}:{secs:02}"
        print(timeformat, end="\r")
        time.sleep(1)
        duration -= 1

    print("Timer ended.")


countdown(60)
