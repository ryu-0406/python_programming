# dictionary
d = {'x': 10, 'y': 20}
print(type(d))
print(d['x'])
print(d)
d['x'] = 'xxxx'
print(d['x'])
d['z'] = 200
print(d)
d[1]=10000
print(d)
print(dict(a=10, b='20'))


print(dict(a=10, b = 20))

print(dict([('a', 10), ('b', 20)]))

# methood of dictionary
d = {'x':10, 'y':20}
print(d)

d2 = {'x': 1000, 'j':500}
d.update(d2)
print(d)

# copy of dictionary
x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# how to use dictionary
fruit = {
    'apple':100,
    'banana': 200,
    'orange':300,
}
print(fruit['apple'])

list = [
    ['appale', 100],
    ['banana', 200],
    ['orange', 300],]

print(list)