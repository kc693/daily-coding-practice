""" This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0. """

def eXorwhY (x,y,b):
    return x*b + y*abs(b-1)

print(f'function for (32,50,1) returns {eXorwhY(32,50,1)}')
print(f'function for (32,-50,0) returns {eXorwhY(32,-50,0)}')