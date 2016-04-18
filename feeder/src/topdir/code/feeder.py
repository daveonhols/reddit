import praw
import urllib3
import urllib.parse
import sys
import sched, time
import datetime
import threading

REDDIT = praw.Reddit(user_agent='test')
SCHED = sched.scheduler(time.time, time.sleep)
NEXTTIME = time.time()+5

def get():
    global NEXTTIME;
    NEXTTIME+=60*5

    SCHED.enterabs(NEXTTIME,1,get,())

    time=datetime.datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
    entries = REDDIT.get_front_page(limit=100)
    rank = 0;
    http = urllib3.PoolManager(50)

    for entry in entries:
        sym='front_page'
        name=entry.name;
        title=entry.title;

        msg=".u.upd[`reddit;({0};`{1};\"{2}\";\"{3}\";\"{4}\";{5};{6};{7};{8};\"{9}\")]".format(time, sym, name, title.replace('"', '\\"'), entry.subreddit.display_name, rank, entry.gilded, entry.ups, entry.downs, entry.short_link)
        url= 'http://127.0.0.1:10000/?'+ urllib.parse.quote(msg);
        res = http.request('GET',url)
        print(msg.encode("utf-8", "backslashreplace"))
        rank+=1

SCHED.enterabs(NEXTTIME,1,get)
SCHED.run()
