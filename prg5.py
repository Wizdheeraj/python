def add(n1,n2):
    return(n1+n2)
def sub(n1,n2):
    return(n1-n2)
def mul(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return(n1/n2)
n1=int(input("enter operand 1:"))
n2=int(input("enter operand 2:"))
operator=input("enter operator:")

if operator == '+':ans=add(n1,n2)
elif operator == '-':ans=sub(n1,n2)
elif operator == '*':ans=mul(n1,n2)
elif operator == '/':ans=div(n1,n2)
else:
    print("wrong operator or operand")
print(ans)    
