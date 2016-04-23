import datetime


def logInfo(msg):
    logAny(msg,"INFO")

def logDebug(msg):
    logAny(msg,"DEBUG")

def logWarn(msg):
    logAny(msg,"WARN")

def logError(msg):
    logAny(msg,"ERROR")


def logAny(msg, type):
    now=datetime.datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
    write=now+":"+type+":"+msg
    print(write, flush=True)