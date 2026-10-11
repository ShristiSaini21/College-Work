 #add two integers
'''num1 = int(input("enter first integer"))
num2 = int(input("enter second integer"))

result = num1 + num2
print(f"sum: {result}")'''

#substract two integer
'''num1 = int(input("enter first integer: "))
num2 = int(input("enter second integer: "))

result = num1 - num2
print(f"difference: {result}")'''

#multiplication
'''num1 = int(input("enter first integer: "))
num2 = int(input("enter second integer: "))

result = num1*num2
print(f"product: {result}")'''

#divide
'''dividend = int(input("enter dividend: "))
divisor = int(input("enter divisor: "))

quotient = dividend // divisor
remainder = dividend % divisor

print(f"quotient: {quotient}")
print(f"remainder : {remainder}")'''

#square and cube
'''num = float(input("enter a number : "))
square= num**2
cube = num**3
print(f"square : {square}")
print(f"cube : {cube}")'''

#area of reactangle
'''length = float(input("enter length : "))
breadth = float(input("enter breadth : "))
area = length*breadth
print(f"area : {area}")'''

#perimeter of circle
'''import math
radius = float(input("enter radius of the circle : "))
perimeter = 2*math.pi*radius
print(f"perimeter of cirlce : {perimeter}")'''

#swap without using a temporary variable
'''a = input("enter a first variable(a) : " )
b = input("enter a second variable(b) : ")
temp = a
a = b
b = temp
print(f"after swapping : a = {a}, b= {b}")'''

#swap with using a temporary varibable
'''a = int(input("enter first number (a) : "))
b = int(input("enter second number (b) : "))
a,b = b,a
print(f"after swapping : a = {a}, b = {b}")'''

#celsius to farenheit
'''celsius = float(input("enter temperature in celsius : "))
farenheit = (celsius*9/5)+32
print(f"temperature in farenheit : {farenheit}" )'''

#farenheit to celsius
'''farenhiet = float(input("enter temperature in farenhiet : "))
celsius = (farenhiet-32)*5/9
print(f"temperature in celsius : {celsius}" )'''

#calculate interest
'''principal = float(input("enter principal amount : "))
rate = float(input("enter rate interest(%) : "))
time = float(input("enter time period : "))
simple_interest = (principal*rate*time)/100
print(f"simple interest : {simple_interest}" )'''

#compound interest
'''principal = float(input("enter principal amount : "))
rate = float(input("enter rate interest : "))
time = float(input("enter time period : "))
amount = (principal*(1+rate/100)**time)
compound_interest = amount - principal
print(f"compound interest : {compound_interest}" )'''

#km to miles
'''km = float(input("enter distance in kilometers: "))
miles = km*0.621371
print(f"distance in miles : {miles}" )'''

#find remainder
'''dividend = int(input("enter dividend : "))
divisor = int(input("enter divisor : "))
remainder = dividend % divisor
print(f"remainder : {remainder}" )'''

#calculate power
'''base = float(input("enter base number : "))
exponent= int(input("enter exponent : "))
result= base**exponent
print(f"result : {result}")'''

#body mass index
'''weight = float(input("enter weight in kg : "))
height = float(input("enter height in meters : "))
bmi = weight/(height**2)
print(f"body mass index(BMI) : {bmi}")'''

#calculate monthly emi
'''principal = float(input("enter loan amount: "))
annual_rate = float(input("enter annual interest rate(%):"))
tenure_months =int(input("enter loan tenure in months:"))
monthly_rate = annual_rate/(12*100)
emi=(principal*monthly_rate*((1+monthly_rate)**tenure_months)/(((1+monthly_rate)**tenure_months)-1))
print(f"monthly emi:{emi:-2f}")  '''

#percentage in 5 subjects
'''sub1=float(input("enter marks of sub1: "))
sub2=float(input("enter marks of sub2: "))
sub3=float(input("enter marks of sub3: "))
sub4=float(input("enter marks of sub4: "))
sub5=float(input("enter marks of sub5: "))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100
print(f"total marks:{total_marks}/500")
print(f"percentage:{percentage:2f}%")'''

#positive or negative
'''num=float(input("eneter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")'''

#even or odd
'''num=int(input("enter an integer: "))
if num%2==0:
    print(f"{num}is even")
else:
    print(f"{num}is odd")'''

#divisible by 5
'''num=int(input("enter a number: "))
if num%5==0:
    print(f"{num}is divisible by 5")
else:
    print(f"{num}is not divisible by 5")'''

#leap year
'''year=int(input("enter year: "))
if(year%400==0)or(year%4==0 and year%100!=0):
    print(f"{year}is a leap year")
else:
    print(f"{year}is not a leap year")'''

#largest two numbers
'''num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if num1 > num2:
    print(f"largest number:{num1}")
elif num2 > num1:
    print(f"largest number:{num2}")
else:
    print("both numbers are equal")'''

#vowel or consonant
'''char=input("enter a single character:").lower()
if len(char)==1 and char .isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel")
    else:
        print(f"'{char}' is a consonant")
else:
        print("invalid input! please enter an alphabetic character")'''

#largest three number
'''a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))
if a>=b and a>=c:
    print(f"largest number:{b}")
else:
    print(f"largest number:{c}")'''

#uppercase, lowecase and digit
'''ch=input("enter a character:")
if len(ch)==1:
    if ch.isupper():
        print("character is uppercase")
    elif ch.islower():
        print("character is lowercase")
    elif ch.isdigit():
        print("character is a digit")
    else:
        print("character is a special symbol")
else:
        print("please enter only a single character")'''

#number is in a given range
'''num=float(input("enter the number to check:"))
lower=float(input("enter lower limit:"))
upper=float(input("enter upper limit:"))
if lower <= num <= upper:
    print(f"{num}is within the range [{lower},{upper}]")
else:
    print(f"{num}is outside the range [{lower},{upper}]")'''

#num is prime
'''num=int(input("enter positive integer:"))
if num>1:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
else:
        print(f"{num} is not a prime number")'''




