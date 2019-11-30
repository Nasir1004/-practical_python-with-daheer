from operator import itemgetter


user =[

   {'fname': 'Bucky', 'Lname': 'robert'},
   {'fname': 'tom', 'Lname': 'Robert'},
   {'fname': 'bernie', 'Lname': 'zunka'},
   {'fname': 'nasir', 'Lname': 'ibrahim'},
   {'fname':'umar', 'Lname': 'Dalhat'},
   {'fname': 'abbas', 'Lname': 'kabir'},
   {'fname': 'musa', 'Lname': 'ibrahim'},
   {'fname': 'Usman', 'Lname':'Ibrahim'},
   {'fname': 'muhammad', 'Lname': 'Dalhat'},


]

for x in sorted(user, key = itemgetter('fname')):
	print(x)

print('.......')

for x in sorted(user, key =itemgetter('fname', 'Lname')):
	print(x) 
