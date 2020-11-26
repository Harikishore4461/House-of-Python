#Creating The List
my_list = list()
my_list.append(2)
my_list.append(4)
my_list.append(1)
my_list.append(5)
my_list.append(3)

# Remove the last element from the list
my_list.pop()
#Remove the specific element
my_list.remove(2)
#Max num from the list 
maximum = max(my_list)
print(f"Maximum number from the list is {maximum}")
#Min num from the list 
minimum = min(my_list)
print(f"Minimum number from the list is {minimum}")

print(my_list)

#create tuple
my_tuple = ('s','y','r','a','c','a','r','d')

print(my_tuple[::-1])

#converting tuple into list
my_list1 = list(my_tuple)
print(my_list1)