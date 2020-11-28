# ques 9 Create a calculator only on a code level by using condition (Basic arithmetic calculator)
print("Calculator")
print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.divide")

# input choice
a = int(input("enter first number"))
b = int(input("enter second number"))
ch = int(input("enter the choice from 1 to 4"))

if ch == 1:
    c = a + b
    print("sum = ", c)
elif ch == 2:
    c = a - b
    print("difference =", c)
elif ch == 3:
    c = a * b
    print("product =", c)
elif ch == 4:
    c = a / b
    print("quotient =", c)
else:
    print("Invalid Choice")

