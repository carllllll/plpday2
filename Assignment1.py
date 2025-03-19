def calculator():
    num1=float(input("Please enter your first number "))
    operation=input("Please enter your operation: +, /, *, -: ")
    num2=float(input("Please  enter your second number "))
    if operation=="+":
        answer=num1+num2
    elif operation=="/":
        if num1 ==0:
            print("Error division using zero is impossible")
            return
        answer=num1/num2
    elif operation=="*":
        answer=num1*num2
    elif operation=="-":
        answer=num1-num2
    else:
        print("Invalid operation. Please enter +, -, /, or *")
        return
    print("The result is: ", answer)
calculator()


