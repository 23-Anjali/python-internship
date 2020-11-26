#ques1 wap to create a list of n integer values and do the following:
# add an item in to the list(using function)
#using append
numbers = [1,2,3]
numbers.append(4)
print(numbers)

#using insert
numbers.insert(3,8)
print(numbers)



print("********")


#delete (using function)
#using clear
numbers.clear()
print(numbers)

#using pop
number=[11,23,24,25]
print(number.pop(3))
print(number)
print("*******")

#using remove
number.remove(23)
print(number)


#store the largest number from the list to a variable

list1 = [10,20,3,90]
a=max(list1)
print(a)

#store the smallest number from the list to a varibale
list1 = [10,20,3,90]
b=min(list1)
print(b)


#2.Create a tuple and print the reverse of the created tuple
tuple1= (1,2,"hello",3,4,5)
print(tuple1)
#reverse
a= tuple1[::-1]
print(a)


#create a tuple and convert tuple into list
tuple2 = ("a","b","c")
c=list(tuple2)
print(c)