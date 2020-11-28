#updating the list
l1=list(range(1,11))
print(f"list:{l1}")
l1=[i+2 for i in l1]
print(f"after updating the list:{l1}")

#pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

#fibonacci series
a,b,s=0,1,0
n=int(input("Enter the no of terms"))
for i in range(i,n+1):
    print(s,end=" ")
    a=b
    b=s
    s=a+b

#Armstrong number
n=input("Enter the number")
n1=list(n)
no=int(n)
n2=[int(i) for i in n1]
l=len(n2)
n3=[pow(i,l) for i in n2]
if sum(n3) == no:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

#Multiplication table of 9
i=9
for j in range(1,11):
    print(f"{i}*{j}={i*j}")

#To check whether a no. is positive or negative
n=int(input("Enter a number"))
if n > 0: print("Positive")
else : print("Negative")

#days to ages
d=int(input("Enter no of days"))
print(f"The age is:{d//365}")

#trigonometry using math functions
import math
s=math.sin(90)*2+math.cos(90)*2
print(f"(sin90)^2+(cos90)^2={s}")

#Simple calculator
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Select the operator:*,+,-,/")
if c=='':print(f"{a}{b}={a*b}")
elif c=='/':print(f"{a}/{b}={a/b}")
elif c=='+':print(f"{a}+{b}={a+b}")
elif c=='-':print(f"{a}-{b}={a-b}")