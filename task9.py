#multiply two arguments
z=lambda x,y:x*y
print(z(2,5))

#fibonacci series
def fib(n):
    r=[0,1]
    any(map(lambda _:r.append(r[-1]+r[-2]),range(2,n)))
    print(r)
n=int(input("Enter number"))
fib(n)

#multiply a number to the list
l=list(range(10))
l=list(map(lambda n:n*3,l))
print(l)

#divisible by 9
l=list(range(90))
l1=list(filter(lambda n:(n%9==0),l))
print(l1)

#count of even no.
l=list(range(1,11))
c=len(list(filter(lambda n:(n%2==0) ,l)))
print(c)