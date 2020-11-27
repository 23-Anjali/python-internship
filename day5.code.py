# ques 1 Create a function getting two integer inputs from users and print the following
# Addition of two numbers is +value
a = int(input("Enter the first value:"))
b= int(input("Enter the second value:"))
def add(x,y):
    c = x+y
    return c
print("The sum is" ,add(a,b))


# subtraction of two numbers is +value
a = int(input("Enter the first value:"))
b= int(input("Enter the second value:"))
def sub(x,y):
    c = x-y
    return c
print("The subtraction is" ,sub(a,b))

# Division of two numbers is +value
a = int(input("Enter the first value:"))
b= int(input("Enter the second value:"))
def div(x,y):
    c = x/y
    return c
print("The division is" ,div(a,b))

# Multiplication of two numbers is +value
a = int(input("Enter the first value:"))
b= int(input("Enter the second value:"))
def mul(x,y):
    c = x*y
    return c
print("The sum is" ,mul(a,b))





# ques2  create a function covid () and it should accept patient name , and body temperature, by default the bpdy temperature should be 98 degree

name = input("enter the name of the patient")
def covid(patientname,temp=98):

    return(patientname ,temp)
print("patient is", covid(name))