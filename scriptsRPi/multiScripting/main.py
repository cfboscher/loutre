import threading

class monThread(threading.Thread):
	def __init__(self,name):
		super(monThread,self).__init__()
		self.name=name

	def run(self):
		execfile(self.name)

t1=monThread("./a.py")
t2=monThread("./b.py")
t1.start()
t2.start()
t1.join()
t2.join()

