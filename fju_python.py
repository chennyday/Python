'''
a = eval(input('Please enter integer a: '))
b = eval(input('Please enter integer b: '))
print('Sum =', a + b, '\nAverage =', (a+b/2))
'''

'''
a = eval(input('Please enter integer a: '))
b = eval(input('Please enter integer b: '))
total = a + b
average = total / 2
print('a =', a, 'b =', b)
print('Total =', total, 'Average =', average)
'''
'''
F = eval(input('Enter temperature(F):'))
C = 5 / 9 * (F - 32)
print('F:', F, '=', 'C:', C)
'''

'''
mile = eval(input('How fast do you pitch(mile)?'))
km = mile * 1.6
print(mile, 'mile =', km, 'km')
'''

'''
pound = eval(input('How much do you weigh(pound)?'))
kg = pound * 0.45
print(pound, 'pound =', kg, 'kg')
'''

'''
ft = eval(input('How tall are you(ft)?'))
inch = eval(input('How tall are you(in)?'))
cm = ft * 12 * 2.54 + inch * 2.54
print(ft, 'ft', inch, 'inch= ', cm, 'cm')
'''

'''
num = eval(input("Please enter an integer: "))
if num > 0:
    print(num, "is positive")
print("Over")
'''

'''
num = eval(input("Please enter an integer: "))
if num > 0:
    print(num, "is positive")
else: 
    print(num, "is negative")
print("Over")
'''

'''
num = eval(input("Please enter an integer: "))
if num > 0:
    print(num, "is positive")
elif num < 0: 
    print(num, "is negative")
else: 
    print(num, "is zero")
print("Over")
'''

'''
num = eval(input("Please input your id:"))
if num == 1:
    print("You are a freshman")
elif num == 2:
    print("You are a sophomore")
elif num == 3:
    print("You are a junior")
elif num == 4:
    print("You are a senior")
else:
    print("Invalid id")
print("Over")
'''

'''
kg = eval(input("How much do you weigh?(kg): "))
cm = eval(input("How tall are you?(cm): "))
m = cm / 100
bmi = kg / m**2
print("You bmi is", '%.2f'%(bmi))
if bmi < 18.5:
    print("Too thin")
elif bmi < 25:
    print("Standard")
elif bmi <30:
    print("Too fat")
else: 
    print("Obese")
''' 
'''
import random
num = random.randint(1, 100)
if num >= 50:
    print(num, "is greater than or equal to 50")
else:
    print(num, "is smaller than 50")
'''
'''
import random
num = random.randint(1, 100)
if num % 3 == 0:
    print(num, 'is a multiple of 3')
if num % 5 == 0:
    print(num, 'is a mulitple of 5')
if num % 3 != 0 and num % 5 !=0:
    print(num, 'is not a multiple of 3 or 5')
'''
'''
year = eval(input('Please enter a year(example 1900):'))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
'''
'''
total = 0
i = 1
while i <= 100:
    total += i
    print('i =', i, 'total =', total)
    i += 1
'''  
'''
#1-100 random, star after even
import random
odd = 0
even = 0
for i in range(100):
    rd = random.randint(1, 100)
    if i >= 1 and i % 10 == 0:
        print()
    if rd % 2 == 0:
        even += 1
        print('%4d*'%(rd), end = '')
    else:
        odd +=1
        print('%4d'%(rd), end = ' ')
print('\nEven: %d\nOdd:%d'%(even, odd))
'''
'''
import random
odd = 0
even = 0
star = 0
for i in range(100):
    rd = random.randint(1, 100)
    if i >= 1 and i % 10 == 0:
        print()
    if rd % 2 == 0:
        even += 1
        star += 1
        print('%3d(%2d)'%(rd, star), end = ' ')
    else:
        odd +=1
        print('%3d    '%(rd), end = ' ')
print('\nEven: %d\nOdd:%d'%(even, odd))
'''
'''
total = 0
for i in range (1, 101):
    total += i
print(total)

i = 0
total = 0
while i < 100:
    i += 1
    total += i
print(total)
'''
'''
for i in range (1,10):
    for j in range (1, 10):
        print('%dx%d=%2d'%(i, j, i*j), end = ' ')
    print()
'''
'''
a = eval(input("Please enter three edges: "))
print(a[0])
print(a[1])
print(a[2])
'''
'''
print(format('hello', '10s'), format('world', '10s'))
print(format(1, '<10d'), format(2.2, '>10.2f'))
'''
'''
x = 123.456
y = 1234567.890
z = 1.23
print('%13.1f %12.1f %12.1f'%(x, y, z))
print('%13.1f %12.1f %12.1f'%(y, z, x))
print('%13.1f %12.1f %12.1f'%(z, x, y))
'''
'''
gcd = 1
k = 2
num1, num2 = eval(input('Enter two numbers: '))

while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        gcd = k
    k += 1
    #print('gcd is %d, k is %d'%(gcd, k))
print('gcd(%d, %d) is %d'%(num1, num2, gcd))
#print('gcd is', gcd)
'''
'''
b, a = eval(input('Enter b/a: (b, a)'))
d, c = eval(input('Enter d/c: (d, c)'))
num1 = b * c + a * d
num2 = a * c
print('%d/%d + %d/%d = %d/%d'%(b, a, d, c, num1, num2))
gcd = 1
k = 2
while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        gcd = k
    k += 1
print('gcd(%d, %d) is %d'%(num1, num2, gcd))
print('%d/%d + %d/%d = %d/%d'%(b, a, d, c, num1/gcd, num2/gcd))
'''
'''
def printStar():
    for i in range(62):
        print('*', end = '')
    print()

def multitable():
    for i in range(1, 10):
        for j in range(1, 10):
            print('%d*%d=%2d'%(j, i, i*j), end = ' ')
        print()

def main():
    printStar()
    multitable()
    printStar()
        
main()
'''
'''
def printStar(n):
    for i in range(n):
        print('*', end = '')
    print()

def multitable():
    for i in range(1, 10):
        for j in range(1, 10):
            print('%d*%d=%2d'%(j, i, i*j), end = ' ')
        print()

def main():
    printStar(60)
    multitable()
    printStar(50)
        
main() 
'''
'''
def total():
    total = 0
    for i in range(101):
        total += i
    return total

def oddsum():
    total = 0
    for i in range(1, 101, 2):
        total += i
    return total

def evensum():
    total = 0
    for i in range(2, 101, 2):
        total += i
    return total

def main():
    print(total())
    print(oddsum())
    print(evensum())

main()    
'''
'''
def total(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)

def oddsum(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    print(total)

def evensum(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    print(total)

def main():
    total(200)
    oddsum(300)
    evensum(200)

main()
'''
'''
def total(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def oddsum(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    return total

def evensum(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total

def main():
    print(total(200))
    print(oddsum(300))
    print(evensum(100))

main()
'''
'''
def total(m, n):
    total = 0
    for i in range(m,n +1):
        total += i
    return total

def oddsum(m, n):
    total = 0
    for i in range(m, n+1, 2):
        total += i
    return total

def evensum(m, n):
    total = 0
    for i in range(m, n+1, 2):
        total += i
    return total

def main():
    print(total(2,101))
    print(oddsum(3, 101))
    print(evensum(10, 102))

main()
'''
'''
def sumAndAverage(m, n):
    total = 0
    for i in range(m, n+1):
        total += i
    average = total / (n-m+1)
    return total, average
def main():
    f, t = eval(input('Enter from and to: '))
    total, average = sumAndAverage(f, t)
    print('Total =', total, ', Average =', average)

main()
'''
'''
i = 1
total = 0
while True:
    total += i
    if total >= 2601:
        break
    i += 2
print('number =', i)
print('total =', total)
'''
'''
a, b, c = eval(input('Enter three numbers: '))
print(a, end = '')
print(str(b+c))
'''
'''
times = eval(input('Times to execute: '))
for i in range(times):
    a = input('Alphabet: ')
    b = input('Number: ')
    c = input('Number: ')
    print(a+str(int(b)+int(c)))
'''
#1. 沒有傳參數，也沒有回傳值
'''
def sum():
    total = 0
    for i in range(1, 101):
        total += i
    print('Total = %d'%(total))

def main():
    sum()
    
main()
'''
#2. 有傳參數，但沒有回傳值
'''
def sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    print('Total = %d'%(total))

def main():
    sum(100)
    
main()
'''
#3. 沒有傳參數，但有回傳值
'''
def sum():
    total = 0
    for i in range(1, 101):
        total += i
    return total

def main():
    print(sum())

main()
'''
#4. 有傳參數，也有回傳值
'''
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def main():
    num = eval(input('Enter an interger: '))
    print(sum(num))
    
main()
'''
'''
def sum(n1, n2):
    total = 0
    for i in range(n1, n2+1):
        total += i
    return total
def main():
    num1, num2 = eval(input('Enter two integers: '))
    if num1 > num2:
        num1, num2 = num2, num1
    tot = sum(num1, num2)
    print('Total =', tot)

main()
'''
'''
def leapyear(y1, y2):
    for year in range(y1, y2):
        cond1 = year % 400 == 0
        cond2 = year % 4 == 0
        cond3 = year % 100 != 0
        if cond1 or cond2 and cond3:
            print(year, end = ' ')
        
def main():
    year1, year2 = eval(input('Please enter two years: '))
    if year1 > year2:
        year1, year2 = year2, year1
    leapyear(year1, year2)

main()
'''
#lst[start:end:interval]
#access from lst[start] to lst[end-1]
#if index is negative
#then in dex + length of lst

'''
lst = [1, 2, 3, 4, 5, 6]
print(lst[2:5])
print(lst[2:-1])
print(lst[-4:-2])
print(lst[::-1])
print(lst[::2])
'''
'''
lotto = []
i = 0
import random
while i <= 6:
    num = random.randint(1, 49)
    if num not in lotto:
        lotto.append(num)
        i += 1
lotto.sort()
print(lotto)
'''
'''
import random
print(random.sample(range(1, 49), 5))
'''
'''
a = 100
def test(a):
    print(a)
test(30)
'''
'''
a = [1, 2, 3, 4, 5, 10, 20]
for i in a:
    print(i, end = ' ')
print()
for j in range(len(a)):
    print(a[j], end = ' ')
'''
'''
a = [1, 3, 4, 2, 6, 3,2, 1, 3, 1]
b = []
b = sorted(a)
print(a)
print(b)
'''
'''
a = [1, 4, 3]
b = [3, 2, 1]
b = a
c = a.copy()
b[1] = 231
print(a)
print(b)
print(c)
'''
'''
items = 'Apple Boy Cat Wow'.split()
print(items)
date = '2020/12/4'.split('/')
print(date)

print(items[0])
print(len(items))
print(items[-2])
print()

for i in items:
    print(i)

print()
print(items)
for i in range(len(items)):
    print('items[%d]=%s'%(i, items[i]))

print()
'''
'''
s = input('Enter 10 numbers seperated by space:')
nums = s.split()
print(nums)
lst = [eval(x) for x in nums]
print(lst)
'''
'''
def sumoflist(m):
    tot = 0
    for i in m:
        tot += i
    return tot

def main():
    lst = [1, 2, 3, 4, 5]
    total = sumoflist(lst)
    print(total)

main()

def sumoflist(m):
    tot = ''
    for i in m:
        tot = tot + i
    return tot

def main():
    lst = ['a', 'b', 'c', 'd', 'e']
    total = sumoflist(lst)
    print(total)

main()
'''
'''
def sumoflist(m):
    tot = 0
    for i in range(len(m)):
        tot += m[i]
    return tot

def main():
    lst = [1, 2, 3, 4, 5]
    total = sumoflist(lst)
    print(total)

main()
'''
'''
def linearsearch(lst2, key):
    for i in range(len(lst2)):
        if key == lst2[i]:
            return i
    return -1

def main():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = linearsearch(lst, 4)
    print('4 is in index of', index)
    index = linearsearch(lst, 9)
    print('9 is in index of', index)
    index = linearsearch(lst, 10)
    print('10 is in index of', index)

main()
'''
'''
def binarysearch(lst2, key):
    low = 0
    high = len(lst2) -1
#    count = 0
    while high >= low:
        mid = (low+high)//2
#        count += 1
#        print(count)
        if key <lst2[mid]:
            high = mid -1
        elif key == lst2[mid]:
            return mid
        else:
            low = mid +1
    return -1

def main():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = binarysearch(lst, 4)
    print('4 is in index of', index)
    index = binarysearch(lst, 9)
    print('9 is in index of', index)
    index = binarysearch(lst, 10)
    print('10 is in index of', index)

main()


def binarysearch(lst2, key):
    low = 0
    high = len(lst2) -1
    count = 0
    while high >= low:
        mid = (low+high)//2
        count += 1
        if key <lst2[mid]:
            high = mid -1
        elif key == lst2[mid]:
            print('Count =', count)
            return mid
        else:
            low = mid +1
    print('Count =', count)
    return -1

def main():
    lst = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    lst.sort()
    print('\nSearching 4...')
    index = binarysearch(lst, 4)
    print('4 is in index of', index)
    print('\nSearching 9...')
    index = binarysearch(lst, 9)
    print('9 is in index of', index)
    print('\nSearching 10...')
    index = binarysearch(lst, 10)
    print('10 is in index of', index)

main()
'''
#2020/12/4 test
#1
'''
def leapyear(m, n):
    for year in range(m, n+1):
        cond1 = year % 400 == 0
        cond2 = year % 4 ==0 and year % 100 != 0
        if cond1 or cond2:
            print(year)
def main():
    year1, year2 = eval(input('Enter two years: '))
    leapyear(year1, year2)
main()
'''
#2
'''
def leapyear(m, n):
    if m > n:
        m, n = n, m
    count = 0
    for year in range(m, n+1):
        cond1 = year % 400 == 0
        cond2 = year % 4 ==0 and year % 100 != 0
        if cond1 or cond2:
            print(year, end = ' ')
            count += 1
            if count % 5 == 0:
                print()
        

def main():
    year1, year2 = eval(input('Enter two years: '))
    leapyear(year1, year2)
main()
'''
#3
'''
def leapyear(year):
    cond1 = year % 400 == 0
    cond2 = year % 4 ==0 and year % 100 != 0
    if cond1 or cond2:
        return True
    else:
        return False


def main():
    count = 0
    year1, year2 = eval(input('Enter two years: '))
    if year1 > year2:
        year1, year2 = year2, year1
    for i in range(year1, year2 +1, 1):
        leapyear(i)
        if leapyear(i) == True:
            count += 1
            print(i, end = ' ')
            if count % 5 == 0:
                print()
#        print('(%d)'%(count), end = ' ')

main()
'''
#4
'''
import random
lst = []
i = 0
while i < 6:
    num = random.randint(1, 49)
    if num not in lst:
        lst.append(num)
        i += 1
lst.sort()
print(lst)
'''
'''
found = False
lst = [10, 4, 2, 78, 90, 23, 12]
print(lst)
key = eval(input('Enter a number: '))
for i in range(len(lst)):
    if lst[i] == key:
        found = True
        print(key, 'at index of', i)
if found == False:
    print(key, 'is not found')
'''
#selection sort
'''
lst = [10, 4, 2, 78, 90, 23, 12]
for i in range(len(lst)-1):
    min = lst[i]
    minIndex = i
    for j in range(i+1, len(lst)):
        if lst[j] < min:
            min = lst[j]
            minIndex = j
    if minIndex != i:
        lst[minIndex] = lst[i]
        lst[i] = min
print(lst)
'''
'''
lst = []
count = 0
import random
for i in range(100):
    num = random.randint(1, 100)
    lst.append(num)
minimum = lst[0]
minIndex = 0
for j in range(0, len(lst)):
    if lst[j] < minimum:
        minimum = lst[j]
        minIndex = j
for k in range(len(lst)):
    if k == minIndex:
        print('%3d*'%(lst[k]), end = '')
    else:
        print('%3d'%(lst[k]), end = ' ')
    count += 1
    if count % 10 == 0:
        print()
print('\nMinimum value is', minimum, 'at index of', minIndex)
'''
'''
lst = []
count = 0
import random
for i in range(100):
    num = random.randint(1, 100)
    lst.append(num)
minimum = lst[0]
minIndex = 0
for j in range(0, len(lst)):
    if lst[j] < minimum:
        minimum = lst[j]
        minIndex = j
for k in range(len(lst)):
    if lst[k] == minimum:
        print('%3d*'%(lst[k]), end = '')
    else:
        print('%3d'%(lst[k]), end = ' ')
    count += 1
    if count % 10 == 0:
        print()
print('\nMinimum value is', minimum)
for s in range(0, len(lst)):
    if lst[s] == minimum:
        print('at index of', s)
'''
'''
times = int(input('How many times: '))
for i in range(times):
    total = 0
    number = (input('Input in binary: '))
    sequence = number[::-1]
    for j in range(len(sequence)):
        total += int(sequence[j]) * (2 ** j)
    print(total)
'''
'''
for i in range(int(input('How many times: '))):
    num = int(input('Input a number: '))
    total = ''
    while num >0:
        total += str(num%2)
        num //= 2
    print(total[::-1])
'''
'''
#complete list
lst2 = [[1, 2],
        [3, 4],
        [5, 6]]

print('number of rows:', len(lst2))
print('number of columns:', len(lst2[0]))

for i in range(len(lst2)):
    for j in range(len(lst2[0])):
        print(lst2[i][j])
print()

for i in range(len(lst2)):
    for j in range(len(lst2[0])):
        print('lst2[%d][%d]=%d'%(i, j, lst2[i][j]))
print()
'''
'''
#skewed list
lst2 = [[1, 2, 3],
        [4],
        [5, 6]]

print('number of rows:', len(lst2))
print('number of columns at index of 0:', len(lst2[0]))
print('number of columns at index of 1:', len(lst2[1]))
print('number of columns at index of 2:', len(lst2[2]))

for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        print(lst2[i][j])
print()

for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        print('lst2[%d][%d]=%d'%(i, j, lst2[i][j]))
    print()
print()
'''
'''
lst2 = [[1, 2],
        [3, 4],
        [5, 6]]

#version 1
for i in range(len(lst2)):
    for j in range(len(lst2[0])):
        print('lst2[%d][%d]=%d'%(i, j, lst2[i][j]))
print()

#version 2
print(lst2)

#version3
total = 0
for row in lst2:
    for data in row:
        total += data
print('total =', total)
'''
'''
lst = [1, 23, 67, 2, 52, 8, 9]
print('length of list: ', len(lst))
print('max value: ', max(lst))
print('min value: ', min(lst))
print('sum of list:', sum(lst))

maximum = lst[0]
for i in range(len(lst)):
    if lst[i] > maximum:
        maximum = lst[i]
print('max value of list is', maximum)

minimum = lst[0]
for i in range(len(lst)):
    if lst[i] < minimum:
        minimum = lst[i]
print('min value of list is', minimum)
'''
'''
lst = [1, 23, 67, 2, 52, 8, 9]
print('length of list: ', len(lst))
print('max value: ', max(lst))
print('min value: ', min(lst))
print('sum of list:', sum(lst))

maximum = lst[0]
index = 0
for i in range(len(lst)):
    if lst[i] > maximum:
        maximum = lst[i]
        index = i
print('max value of list is', maximum, 'at index', index)
print()

Max = max(lst)
print(lst.index(Max))
'''
'''
lst3 = [[1, 23, 67], [2, 52], [8, 9, 100, 11]]

maximum = lst3[0][0]
index = (0, 0)
for i in range(len(lst3)):
    for j in range(len(lst3[i])):
        if lst3[i][j] > maximum:
            maximum = lst3[i][j]
            index = (i, j)

print('max value is', maximum, 'at index', index)
'''
'''
lst2 = []
row = eval(input('How many rows: '))
col = eval(input('How many columns: '))
count = 0
for i in range(row):
    lst2.append([])
    for j in range(col):
        count += 1
        data = eval(input('Input data #%d: '%(count)))
        lst2[i].append(data)
print(lst2)
'''
'''
import random
lst2 = []
row = eval(input('How many rows: '))
col = eval(input('How many columns: '))
count = 0
for i in range(row):
    lst2.append([])
    for j in range(col):
        data = random.randint(1, 100)
        lst2[i].append(data)
print(lst2)
print()

d = lst2.pop()
print('deleted data is', d)
print(lst2)
print()

d2 = lst2[0].pop()
print('deleted data is', d2)
print(lst2)
print()

d3 = lst2[1].pop(0)
print('deleted data is', d3)
print(lst2)
print()
'''
'''
import random
lst2 = []
row = eval(input('How many rows: '))
col = eval(input('How many columns: '))
count = 0
for i in range(row):
    lst2.append([])
    for j in range(col):
        data = random.randint(1, 100)
        lst2[i].append(data)
print(lst2)
print()

for i in range(len(lst2)):
    total = 0
    for j in range(len(lst2[i])):
        total += lst2[i][j]
    print('Total of #%d row is %d'%(i+1, total))
print()

for i in range(col):
    total = 0
    for j in range(row):
        total += lst2[j][i]
    print('Total of #%d column is %d'%(i+1, total))
'''
'''
def agree():
    return True
def disagree():
    return False

if agree():
    print('yes')
else:
    print('no')

if disagree():
    print('yes')
else:
    print('no')
'''
'''
def echo(something):
    return something + " " + something
print(echo('abc'))


def echo(something):
    something += '123'
    return something + " " + something
print(echo('abc'))
'''
'''
def add(num1, num2):
    return num1 + num2
def mult(num1, num2):
    return num1 * num2

print(add(1, 2))
print(mult(2, 3))

print(add(5, mult(5, 6)))
'''
'''
n = int(input(': '))
num = []
while True:
    a = n // 2
    b = n % 2
    num.append(str(b))
    n = a
    if a == 0:
        break
a = ''.join(num[::-1])
print(a)
'''





