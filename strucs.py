from struct import *

#store as bytes data
packed_data = pack('iif', 6, ,19, 4.73)
print(packed_data)


print(calcsize('i'))
print(calcsize('f'))
print(calcsize('lif'))

# to get bytes data back to normal (b')

original_data = unpack('lif', packed_data)
print(original_data)

print(unpack('lif',b'/x06\))
