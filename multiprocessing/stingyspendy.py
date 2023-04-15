from threading import Thread, Lock
import time


class StingySpendy:
  money = 100
  mutex = Lock()

  def stingy(self):
    for _ in range(100_000):
      StingySpendy.mutex.acquire()
      StingySpendy.money += 1
      StingySpendy.mutex.release()
    print("Stingy done")

  def spendy(self):
    for _ in range(100_000):
      StingySpendy.mutex.acquire()
      StingySpendy.money -= 1
      StingySpendy.mutex.release()
    print("Spendy done")


ss = StingySpendy()
Thread(target=ss.stingy).start()
Thread(target=ss.spendy).start()

time.sleep(5)
# Global Interpreter Lock (GIL)
print(StingySpendy.money)
