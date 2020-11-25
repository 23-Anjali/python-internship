# Ques 1 Write a python program to merge two python dictionaries
dic1 = {"a":20,"b":30}
dic2 = { "c":40 , "d": 50}
d = dic1.copy()
d.update(dic2)
print(d)

# Ques 2 Write a python program to remove a key from dictionaries
user = {
        'name':'anjali',
        'age': 19 ,
        'college': 'DIT'
}
print( user.pop("age"))
print (user)      # key is deleted
# Ques 3 Write a python program to map to list into a dictionaries
keys = ['red', 'green','blue']
values= ["$3456, $5678, $3215"]
color_codes= dict(zip(keys,values))
print(color_codes)

# Ques 4 Write a python program to find the length of a set

s={1,2,3,7,8,45,65,43}
print(len(s))


# Ques 5 Write a python program to remove the intersection of a 2nd set from the 1st set

s1= {1,7,8,4}
s2= {4.8,9,7}
print("original set")
print(s1)
print(s2)
print("removing the intersection")
s1.difference_update(s2)
print(s1)
#or we can also use
print(s1-s2)
