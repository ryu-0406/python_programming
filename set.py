# what is set
a = {1, 2, 3 ,4 ,4, 4, 5, 6}
print(a)
print(type(a))
b = {2, 3, 6, 7}
print(b)
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)

s = {1, 2, 3, 4, 5}
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)

help(set)

# how to use set
my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

