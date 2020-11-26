d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5}
d3={**d1,**d2}
print(f"after merging two dictionary:{d3}")

del d3["a"]
print(f"after deleting a key:{d3}")

l1=["f","g","h"]
l2=[6,7,8]
d4=dict(zip(l1,l2))
print(f"after mapping two lists to a dictionary:{d4}")

s1={"w","x","y","z"}
print(f"length of set:{len(s1)}")

s2={"z","a","b","c"}
print(f"after removing the intersection of 2nd set from 1st set:{s1-s2}")