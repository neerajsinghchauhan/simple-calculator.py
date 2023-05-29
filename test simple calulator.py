def prompt_menu():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    print("""
the  list of operators are: 
1. Addition
2. Subtraction
3. Multiplication
4. Divide
5. division with remainder
""")
    op = int(input("enter an operator no: "))
    return a, b, op

def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("sum: {} + {} = {}".format(a,b,a+b))
    elif op == 2:
        print("subtraction: {} - {} = {}".format(a,b,a-b)) 
    elif op == 3:
        print("multiply: {} * {} = {}".format(a,b,a*b))
    elif op == 4:
        print("divide: {}/{} = {}".format(a,b,a/b))
    elif op == 5:
        try:
            print("division with remainder: {}//{} = remainder:{}".format(a,b,a//b,a%b))
        except:
            print("division by zero not possible")
    
    else:
        print("like that no  choice available ") 
    loop()

def loop():
    choice = input("do you want to calculate further? (YES OR NO):  ")
    if choice.upper() == "YES":
        calculate()
    elif choice.upper() == "NO":
        print("good buy and Thank You.") 
    else:
        print("like that no choice available")
        loop()

calculate()









    