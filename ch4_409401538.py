#p120
#4.1
'''
a, b, c = eval(input('Enter a, b, c: '))
D = b**2 - 4*a*c
root1 = (-b + (b**2 - 4*a*c)**(0.5))/ (2*a)
root2 = (-b - (b**2 - 4*a*c)**(0.5))/ (2*a)
if D < 0:
    print('The equation has no real roots.')
elif D == 0:
    print('The root is', root1)
else:
    print('Roots are %f, and %f'%(root1, root2))
'''
#4.3
'''
a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))
if a*d - b*c == 0:
    print('The equation has no solution.')
else:
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    print('x is %.1f and y is %.1f'%(x, y))
'''
#4.19
'''
a, b, c = eval(input('Enter three edges: '))
if b + c > a and a + c > b and a + b > c:
    p = a + b + c
    print('The perimeter is %d'%(p))
else:
    print('The input is invalid')
'''
#4.22
'''
x, y = eval(input('Enter a point with two coordinates: '))
d = (x ** 2 + y ** 2) ** 0.5
if d <= 10:
    print('Point (%.1f, %.1f) is in the circle'%(x, y))
else:
    print('Point (%.1f, %.1f) is not in the circle'%(x, y))
'''
#4.26

number = eval(input(':'))
a = number // 100
b = number % 10
if a == b:
    print('yes')
else:
    print('no')





