t = (1, 2, 3, 4, 1, 2)
print(t)
print(t)
print(t[-1])
print(t[2:5])
t.index(1)
t.index(1, 1)
t.count(1)
print(help(list))
print(help(tuple))

t = ([1, 2, 3], [4, 5, 6])
print(t)
print(t[0][0])
t = 1,
print(type(t))
t = ()
print(type(t))
new_tuple = (1, 2, 3) + (4, 5, 6)

# unpacking of tuple
num_tuple = (10, 20)
print(num_tuple)
x, y = num_tuple
print(x, y)
print(x)

min, max = 0, 100
print(min, max)

i = 10
j = 20
temp = i
i = j
j = temp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# when to use tuple
choose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('B')

print(choose_from_two)
print(answer)
