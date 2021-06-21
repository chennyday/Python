#1.10
'''
mile = 14 / 1.6
hr = 60*60
time = 45*60 + 30
per = mile * (hr / time)
print(per)
'''
#1.11
'''
ppl = 312032486 + 5*(-365*24*60*60/13 + 365*24*60*60/7 + 365*24*60*60/45)
a = round(ppl)
print(a)
'''
#2.12
num = eval(input('Enter an integer: '))
thousands = num//1000
hundreds = num//100%10
tens = num//10%10
units = num%10

print(thousands, hundreds, tens, units)

#2.22
'''
yrs = eval(input('Enter the number of years: '))
ppl = 312032486 + yrs*(-365*24*60*60/13 + 365*24*60*60/7 + 365*24*60*60/45)
a = round(ppl)
print(a)
'''

