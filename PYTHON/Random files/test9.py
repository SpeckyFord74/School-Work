import sys, time

def typing(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

typing("Hello world")
