class enemy:
	def _init_(self, x):
		self.energy = x

	def get_energy(self):
		print(self.energy)


jason = enemy(5)
sandy = enemy(16)

jason.get_energy()
sandy.get_energy()
