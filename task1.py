#1. The Calculator App
#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
#Task 1: Create functions for each arithmetic operation.
#Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
#Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

operation =["+","-","*","/"]
def basic_operation():
    

    while True:
        try:
            print("Welcome to your Calculator")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number:  "))
            task = input("Choose an operation(+,-,*,/)")
            if task not in operation:
    
                print("Invalid opoeration please choose:(+,-,*,/)")

            if task =="+":
                result = num1+num2
            elif task =="-":
                result =num1-num2
            elif task =="*":
                result = num1*num2
            elif task =="/":
                result = num1/num2
            print(F"The result is {result}") 
        except ZeroDivisionError:
            print("Can not divide by zero")
basic_operation()
           
      
        
        

          
        
    
        

    
    
    
        