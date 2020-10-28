import requests
import schedule
from _thread import start_new_thread
import time
# import sleep
# from apscheduler.schedulers.background import BackgroundScheduler
# scheduler = BackgroundScheduler()

threadId = 1 # thread counter
# waiting = 6 # 2 sec. waiting time
# time = 0

def req():
    global threadId
    count = 0
    
    while (count < 8):
        x = requests.get('http://callback.kiapiser.com/jabber/dflash?mod=7&num={}&when=old', count)
        print(x.status_code)
        print(count)
        threadId += 1
        count = count + 1

schedule.every(10).seconds.do(req)

while 1:
    print("Waiting for threads to return...")
    start_new_thread(req, ( ))
    schedule.run_pending()
    time.sleep(2)
# sleep(waiting)
# scheduler.add_job(req, 'interval',  seconds=10)
# scheduler.start()