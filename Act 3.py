def add(a,b):
    return a+b

def sub(a,b):
    return a-b

ch=input("Enter the operator to be used (+/-):")
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))

if ch=="+":
    print("Add:",add(a,b))

elif ch=="-":
    print("Subtract",sub(a,b))

