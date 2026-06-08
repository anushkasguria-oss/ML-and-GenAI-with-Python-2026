#first 10 natural numbers
def natural_number(n):
    for i in range(1,n+1):
        print(i,end=" ")
natural_number(10)

#sum of first n natural numbers
def natural_num(n):
    sum=0
    for i in range (1,n+1):
        sum=sum+i
    print("Sum of no. = ",sum)
n=int(input("Enter no. = "))
natural_num(n)

#reverse a number
def reverse(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print("Reversed no. =", rev)
num=int(input("Enter no. : "))
reverse(num)

#count digit in a number
def count_digit(num):
    count=0
    while num>0:
        count=count+1
        num=num//10
    print("Number of digits =",count)
num=int(input("Enter no. : "))
count_digit(num)

#check palindrome number
def palindrome(num):
    original=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if original==rev:
        print("It is a Palindrome Number")
    else:
        print("It is not a Palindrome Number")

num = int(input("Enter no. : "))
palindrome(num)

#generate fibonacci series
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("No. of terms = "))
fibonacci(n)

#Calculator
def add(a,b):
    print("Addition= ",a+b)
def subtract(a,b):
    print("Subtraction= ",a-b)
def multiply(a,b):
    print("multiplication= ",a*b)
def divide(a,b):
    print("division= ",a/b)

choice=int(input("Enter your choice: "))

a=int(input("Enter first no. : "))
b=int(input("Enter second no. :"))

if choice==1:
    add(a,b)
elif choice==2:
    subtract(a,b)
elif choice==3:
    multiply(a, b)
elif choice==4:
    divide(a,b)
else:
    print("Invalid Choice")
