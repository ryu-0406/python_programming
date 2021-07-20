x = 'a is {}'.format('test')
print(x)

y = 'a is {}{}{}'.format(1, 2, 3)
print(y)

z = 'My name is {0} {1}'.format('Jun', 'Sakai')
print(z)

a = 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Jun', family='Sakai')
print(a)

num = str(1)
print(num, type(num))
