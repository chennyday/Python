#p159
#5.3
'''
print(format('Kilograms', '15s'), 'Pounds')
for i in range (1, 200, 2):
    print(format(i, '<15d'), '%6.1f'%(i*2.2))
'''
#5.4

print(format('Miles', '10s'), 'Kilometers')
for i in range (1, 11):
    print(format(i, '<10d'), '%.3f'%(i*1.609))

#5.14
'''
n = 1
while n ** 2 <= 12000:
    n += 1
print(n)
'''
#5.19
'''
num = eval(input('Enter 1 - 15: '))
for i in range(1, num + 1):
    for j in range(num, 0, -1):
        if i < j:
            print('  ', end = ' ')
        else:
            print('%2d'%(j), end = ' ')
    for k in range(2, i+1):
        print('%2d'%(k), end = ' ')
    print()
''' 
#5.20
'''
print('Pattern A')
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()

print('\nPattern B')
for i in range(1, 7):
    for j in range(1, 8 - i):
        print(j, end = ' ')
    print()

print('\nPattern C')
for i in range(1, 7):
    for j in range(6, 0, -1):
        if j <= i:
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    print()  

print('\nPattern D')
for i in range(1, 7):
    for j in range(i, 1, -1):
        print('  ', end = '')
    for j in range(1, 8 - i):
        print(j, end = ' ')
    print()
'''
#5.26
'''
total = 0
for i in range (1, 98, 2):
    total += i / i + 2
print(total)
'''
#5.27
'''
n = 10001
total = 0
for j in range(1, 11):
    for i in range(n - 10000, n):
        total += (-1) ** (i + 1) / (2 * i - 1)
    print(4 * total)
    n += 10000
'''  

