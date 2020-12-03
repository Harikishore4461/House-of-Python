# program using zip() function and list() function, create a merged list of tuples from the two lists given.
list_1=[1,3,5,7,9]
list_2=[2,4,6,8,10]
x=zip(list_1,list_2)
print(tuple(x))

# create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

num=range(1,8)
list_3=[10,20,30,40,50,60,70,80]
y=zip(num,list_3)
print(tuple(y))

# Using sorted() function, sort the list in ascending order.
list_4=[100,50,455,13,12,10,4,2000]
result=sorted(list_4) #if we want in descending order use ,reverse=True
print(result)

# program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list_5=[1,2,3,4,5,6,7,8,9,10,11,12]
new_list=list(filter(lambda x:(x%2!=0),list_5))
print(new_list)