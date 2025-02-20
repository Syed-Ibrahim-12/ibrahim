
def add(x, y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mul(x,y):
    return x*y

def perform(x, y, z):
    if operator == "+":
        answer = add(num1,num2)
        print(answer)
    elif operator == "-":
        answer = sub(num1,num2)
        print(answer)
    elif operator == "/":
        answer = div(num1,num2)
        print(answer)
    elif operator == "*":
        answer = mul(num1,num2)
        print(answer)
    return answer
while True :
    num1 = int(input("enter fisrt num: "))
    operator = str(input("what you want to perform: "))
    num2 = int(input("enter second num: "))
    answer = 0
    
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        perform(num1, num2, operator)
        ask = input("Do you want to continue: yes or no")
        if ask == "yes":
            continue
        else:
            break
            
       