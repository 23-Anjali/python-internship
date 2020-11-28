#ques 1 write a program to loop through a list of number and add+2 to every value of elements of list

list1= [1,2,3,4,5,6]
for i in list1:
    print(i+2)


#ques 2 Write a program to get the below pattern.
"""5 4 3 2 1
   4 3 2 1
   3 2 1
   2 1
   1"""
row=6
for i in range(0,6):
    for j in range(row-i,0,-1):
        print(j , end='')
    print()

#ques 3 python program to print the Fibonacci sequence.
# '''Fibonacci sequence 0,1,1,2,3,5,8,13......'''
a=0
b=1
c=0
n=int(input("enter the last limit"))
for i in range (2,n):
    c = a+b

    print(c , end= "")
    a=b
    b=c

print("   ")

#ques 4 Explain armstrong number and write a code with a function
# Armstrong number is equal to sum of the cubes of its own digits for example 370 is an armstrong number

num= int(input("enter a number"))
sum=0
temp = num
while(temp > 0):
    digit = temp %10
    sum += digit **3
    temp //=10
if(num == sum):
    print("YES ITS ARMSTRONG")
else:
    print("No its not a armstrong")

#ques 5 WAP to write a multiplication table of 9

for i in range (1,11):
    print(9 ," *" , i , " = ", 9*i)

#ques 6 Check if a number is positive or negative

num = int(input("enter a number"))
if (num > 0):
    print("number is  postive")
else :
    print("number is negative")

#ques 7 WAP to convert the numbers of days to  years
days = int(input("enter the number of days"))
years = days/365
print("numbers of yrs will be ", years)

#ques 8 Solve trignometry problm using math function and WAP to solve using math function
import math
x = 0.75
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print(math.asin(x))

