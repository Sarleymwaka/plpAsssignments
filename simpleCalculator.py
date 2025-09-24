num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
operator=(input("enter operator: "))
if operator == '+':
    result= num1+num2
elif operator == '-':
    result= num1-num2
elif operator == '*':
    result= num1*num2
elif operator == '/':
    if num2==0:
        print("error:division by 0")
        exit()
    result=num1/num2
else:
    print("error:invalid operator")
    exit()
print(num1, operator,num2,"=",result)
