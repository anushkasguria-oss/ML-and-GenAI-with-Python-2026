#sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum=sum+i
print("Sum of first 10 natural no.:",sum)

#Factorial of a number
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial =",fact)

#Fibonacci series
n=int(input("Enter number of terms: "))
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#Find largest 
a=int(input("enter no. : "))
b=int(input("enter no. : "))
c=int(input("enter no. : "))

if a>=b and a>=c:
    print("largest value = ",a)
elif b>=a and b>=c:
    print("largest value = ",b)
else:
    print("largest value = ",c)

#Student result system

#student details
name=input("Enter name of student : ")
roll_no=int(input("Enter roll no. :"))

#marks in each subject
maths=int(input("Enter marks : "))
english=int(input("Enter marks :"))
evs=int(input("Enter marks : "))

#Percentage Calculation
total=maths+english+evs
p=(total/300)*100
print("Percentage = ",p,"%")

#Grade Calculation
if p<=100 and p>=93:
    print("Grade = A ")
elif p<=92 and p>=83:
    print("Grade = B ")
elif p<=82 and p>=73:
    print("Grade = C ")
else:
    print("Grade = D" )