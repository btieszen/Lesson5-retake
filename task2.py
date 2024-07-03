#The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a function to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.

cart=[]
def shopping_list():
    while True:
        print("Welcome to your personilized shopping list")
        print("1. Add items to your shopping list")
        print("2. Remove items from your shopping list")
        print("3. Print out your shopping list")
       
        add = (input(" Please make your selection: "))
        if add == ("1"): 
            add_list=input("What item would you like to add to your shopping list ? ").upper()
            cart.append(add_list)
            print(f"{add_list} has been added to your shopping list")
        elif add ==("2"):
            remove_list=input("What item would you like to remove from your shoppimg list: ").upper()
            if remove_list in cart:
                cart.remove(remove_list)
                print(f"{remove_list} has been removed from your shopping cart")
        elif add ==("3"):
            print(f"Your shopping list is: ")
            for carts in cart:
               print(carts)
       
        else:
            print(f"Invalid entry please try again")
            
shopping_list()
                
        
       
shopping_list(cart)
