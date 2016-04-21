import praw
import urllib3
import urllib.parse
import datetime
import runner
import sys

REDDIT = praw.Reddit(user_agent='User-Agent: praw:com.github.daveonhols.reddit:v0.0.1 (by /u/__d7)')
LISTEN_PORT=int(sys.argv[1])

print(LISTEN_PORT)

def get():

    time=datetime.datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
    entries = REDDIT.get_front_page(limit=500)
    rank = 0;
    http = urllib3.PoolManager(50)

    for entry in entries:
        sym='front_page'
        name=entry.name;
        title=entry.title;

        msg=".u.upd[`reddit;({0};`{1};\"{2}\";\"{3}\";\"{4}\";{5};{6};{7};{8};\"{9}\")]"\
            .format(time,
                    sym,
                    name,
                    title.replace('"', '\\"'),
                    entry.subreddit.display_name,
                    rank,
                    entry.gilded,
                    entry.ups,
                    entry.downs,
                    entry.short_link)

        url= 'http://127.0.0.1:10000/?'+ urllib.parse.quote(msg);

        http.request('GET',url)
        print(msg.encode("utf-8", "backslashreplace"))
        rank+=1

r = runner.Stoppable(get, LISTEN_PORT)
