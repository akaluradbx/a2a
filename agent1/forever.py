# forever.py
import time
import datetime

while True:
    print(datetime.datetime.now(), flush=True)
    time.sleep(15)
