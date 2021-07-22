l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(len(l))
x = list('abcdefg')
print(x)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])
a = ['a', 'b', 'c']
b = [1, 2]
c = [a, b]
print(c)
print(c[0])
print(c[1])
print(c[0][1])

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'x'
print(s)
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
s[:] = []
print(s)

g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(g)
g.append(100)
print(g)
g.insert(0, 200)
print(g.pop())
print(g)
g.pop(0)
print(g)
del g[0]
print(g)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
print(a)
x = [1, 2, 3, 4, 5,]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)


r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))
if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print((r))

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = '####### '.join(to_split)
print((x))

print(help(list))

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

seat = []
min = 0
max = 5
print(min <= len(seat) < max)
print(len(seat))

