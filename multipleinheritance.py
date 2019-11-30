class mario():
	def move(self):
		print('i am moveing')

class shroom():
	def eat_shroom(self):
		print('now i am big')

class bigmario(mario,shroom):
	pass

bm = bigmario()
bm.move()
bm.eat_shroom()
