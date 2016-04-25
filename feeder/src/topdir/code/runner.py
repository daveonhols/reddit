import sys
import traceback
import threading
import datetime
import socket
import sched, time
import log

class Stoppable:

    def PrintTime(self):
        time=datetime.datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]
        log.logInfo(time)

    _isActive=True;
    _scheduler = sched.scheduler(time.time, time.sleep)
    _checkStopFrequency=5;
    _nextTime=time.time()+5;
    _doInterval=0;
    _do=PrintTime
    _listenPort=0;
    _maxFails=0;
    _fails=0

    def __init__(self,job=PrintTime,listenPort=10020, maxFails=5, doInterval=60):
        self._do=job
        self._listenPort=listenPort
        listenThread = threading.Thread(target=self.Listen)
        listenThread.daemon=True
        listenThread.start()
        self._maxFails=maxFails
        self._doInterval=doInterval
        self._scheduler.enter(self._checkStopFrequency, 1, self.CheckOnTimer)
        self._scheduler.enterabs(self._nextTime, 1, self.DoJob)
        self._scheduler.run()

    def handleMsg(self, msg):
        if "stop" == msg:
            self._isActive=False;
            sys.exit()

    def Listen(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', self._listenPort))

        while True:
            sock.listen(1)
            connection, client = sock.accept()
            try:
                msg = connection.recv(1024).decode("utf-8")
                if msg:
                    self.handleMsg(msg)

            finally:
                log.logInfo("cleaning up...")
                connection.close()
                sock.close()


    def CheckShouldStop(self):
        if not self._isActive:
            sys.exit()

    def CheckOnTimer(self):
        self._scheduler.enter(self._checkStopFrequency,1,self.CheckOnTimer)
        self.CheckShouldStop()

    def DoJob(self):
        self.CheckShouldStop()
        self._nextTime+=self._doInterval
        self._scheduler.enterabs(self._nextTime,1,self.DoJob)
        try:
            self._do()
            self._fails=0;
        except BaseException as bex:
            log.logWarn("Job run triggered an error:"+traceback.format_exc())
            self._fails+=1;
            if self._fails > self._maxFails:
                log.logError("Too many errors, will exit:"+traceback.format_exc())
                raise
        finally:
            log.logInfo("Done a loop")
