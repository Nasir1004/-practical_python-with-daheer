import threading

class nasirmessenger(threading.thread):
	def run(self):
		for _ in range(10):
			print(threading.currentthreading().getname())

x = nasirmessenger(name ='send out messenger')
y = nasirmessenger(name='recieve messenger')

x.start()
y.start()
