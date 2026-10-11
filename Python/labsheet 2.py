 #multiple of both 3&7
'''n=int(input("enter number:"))
if n%3==0 and n%7==0:
    print("miltiple of both 3 and 7")
else:
    print("not a multipleof both")'''

#number is palindrome
'''s=input("enter number:")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")'''

#absolute value of a number
'''n=float(input("enter number:"))
print("absolute value:",abs(n))'''

#armstrong number
'''n=int(input("enter number:"))
s=sum(int (d)**len(str(n))for d in str(n))
if n==s:
    print("armstrong number")
else:
    print("not armstrong")'''

#display grade
'''m=int(input("enter marks:"))
if m >=90:
    print("Grade A")
elif m >=75:
    print("Grade B")
elif m >=50:
    print("Grade C")
else:
     print("Grade F")'''

#triangle is valid or not
'''a=int(input("Angle 1:"))
b=int(input("Angle 2:"))
c=int(input("Angle 3:"))
if a+b+c==180 and a>0 and b>0 and c>0:
    print("Valid Traingle")
else:
    print("Invalid Triangle")'''

#type of triangle
'''a=int(input("Side 1:"))
b=int(input("side 2:"))
c=int(input("side 3:"))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")'''

#string contains a particular strings
'''s=input("enter text:")
sub=input("Enter substring:")
if sub in s:
    print("found")
else:
    print("not found")'''

#eligiblity for voting
'''age=int(input("enter age:"))
if age>=18:
    print("eligible")
else:
    print("not eligible")'''

#print number using for loop
'''for i in range(1,11):
    print(i, end=" ")'''

#smallest numbers among three numbers
'''a=int(input("num 1:"))
b=int(input("num 2:"))
c=int(input("num 3:"))
print("smallest:",min(a,b,c))'''

#print 10 to 1 using while loop
'''i=10
while i>=1:
    print(i,end=" ")
    i-=1'''

#sum of first n natural number
'''n=int(input("enter n:"))
s=sum(range(1,n+1))
print("sum:",s)'''

#factorial of given number
'''import math
n=int(input("enter number:"))
print("factorial:",math.factorial(n))'''

#multiplicstion of table
'''n=int(input("enter num:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")'''

#print even number
'''for i in range(2,51,2):
 print(i, end=" ")'''

#print odd number
'''for i in range(1,51,2):
    print(i, end=" ")'''

#fibonacci series
'''n=int(input("enter terms:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b, a+b'''

#reverse number using loop
'''n=int(input("enter num:"))
reverse=0
while n>0:
    reverse = reverse*10+n%10
    n//=10
    print("reversed:",reverse)'''

#count number in a digit
'''n=int(input("Enter number:"))
print("Digit Count:",len(str(abs(n))))'''

#sum of digit
'''n=input("enter number:")
print("sum of digit:",sum(int(d)
for d in n if d.isdigit()))'''

#prime number b/w 1 to 100
'''for n in range(2,101):
    if all(n %i !=0 for i in range(2,int(n**0.5)+1)):
        print(n,end=" ")'''

#number is perfect
'''n=int(input("Enter num:"))
s=sum(i for i in range(1,n)if n%i==0)
if s==n:
    print("Perfect num")
else:
    print("not perfect")'''

#print a pattern
'''n=int(input("Enter rows:"))
for i in range(1,n+1):
    print("*"*i)'''

#reverse pattern
'''n=int(input("Enter rows:"))
for i in range(n,0,-1):
    print("*"*i)'''

#pyramid pattern
'''n=int(input("Enter rows: "))
for i in range(1, n+1):
    print(" " *(n-i)+" " .join (str(j) for j in range(1, i+1)))'''

#display table 1to10
'''for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()'''

#HCF using loop
'''a=int(input ("num 1: "))
b=int(input("num2: "))
while b:
    a,b=b,a%b
    print("HCF:",a)'''

#LCM using loop
'''a=int(input("num 1: "))
b=int(input("num 2: "))
x,y=a,b
while y:
    x,y=y,x%y
lcm=(a*b)//x
print("lcm:",lcm)'''

#Strong number
'''import math
n=int(input("Enter no: "))
s=sum(math.factorial(int(d))for d in str(n))
if s==n:
    print("strong number")
else:
    print("not strong")'''



