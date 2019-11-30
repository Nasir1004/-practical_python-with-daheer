import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'goog', 'price':800},
    {'ticker': 'f', 'price':54},
    {'ticker': 'msft', 'price':313},
    {'ticker': 'TUNA','price':68},

]

print(heapq.nsmallest(2, stocks, key=lambda stocks:['price']))
