from operator import attrgetter

class User:

	def _init_(self, x, y):
		self.name = x
		self.user_id = y 


	def _repr_(self):
		return self.name + ":" + str(self.user_id)


users = [
     User ('nasir', 43),
     User('abbas', 5),
     User('tuna', 61),
     User('brain', 61),
     User('joby', 77),
     User('amanda', 9)
]

for user in users:
	print(user)

print('======')
for user in sorted(users, key = attrgetter('name')):
	print (user)

print('======')
for user in sorted (user , key = attrgetter('name')):
	print(user)
	


