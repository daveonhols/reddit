import socket
import time
import unittest
import runner
import threading

class StubRunnerTestException(BaseException):
    pass

class StubRunner:
    _called=0;
    _throwAfter=0;

    def __init__(self, throwAfter=0):
        self._throwAfter=throwAfter

    def do(self):
        print("Stub runner running...")
        self._called+=1
        if self._called>self._throwAfter:
            raise StubRunnerTestException("Stub runner throwing on demand.")


class TestFeederRunner(unittest.TestCase):

    def testRunnerOnError(self):
        sr = StubRunner(throwAfter=1)

        failed=False
        try:
            runner.Stoppable(job=sr.do, maxFails=2, doInterval=3)
        except StubRunnerTestException as srx:
            self.assertTrue(4==sr._called)#once ok, twice allowed to fail, once to blow up
            failed=True

        self.assertTrue(failed)

    def runAsync(self, stubRunner, maxFails, doInterval):
        runner.Stoppable(job=stubRunner.do, maxFails=maxFails, doInterval=doInterval)


    def testRunnerCanStop(self):
        sr=StubRunner(throwAfter=99)
        thread=threading.Thread(target=self.runAsync, args=(sr, 99, 3))
        thread.start()
        time.sleep(20)
        addr=('127.0.0.1', 10020)
        sock=socket.create_connection(addr)
        sock.sendall(bytes("stop".encode("utf-8")))
        sock.close()
        self.assertTrue(sr._called>4)