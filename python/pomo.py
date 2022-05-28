import sys
import time


def pomo_countdown(duration):
    try:
        while duration:
            mins, secs = divmod(duration, 60)
            timeformat = f"{mins:02}:{secs:02}"
            print(f"🍅 {timeformat}", end="\r")
            time.sleep(1)
            duration -= 1
        print("Timer ended.")

    except KeyboardInterrupt:
        quit()


def help():
    print("Usage: python3 pomo.py start [DURATION]")
    quit()


duration_in_mins = 25


if len(sys.argv) > 1:
    match(sys.argv[1]):
        case "help":
            help()
        case "start":
            if len(sys.argv) > 2:
                pomo_countdown(int(sys.argv[2]) * 60)
            else:
                pomo_countdown(duration_in_mins * 60)
else:
    help()
