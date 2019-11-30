stocks = {
	'goog':  434,
	'apple': 345,
	'fb':    54,
	'amazon': 32,
	'msfi' : 549,


}

#(434, goog) (345, apple)
min_price = min(zip(stocks.value(), stocks.key()))
print(min_price)
