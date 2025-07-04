# open "menu" option

def menu():
    print("Welcome to the XYZ Food Service!")
    print("Please select an option:")
    meal_types = ["Breakfast", "Lunch", "Dinner"]
    for i, meal in enumerate(meal_types):
        print(f"{i+1}. {meal}")
    

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        print("You have selected Breakfast.")
        breakfast()
    elif choice == '2':
        print("You have selected Lunch.")
        lunch()
    elif choice == '3':
        print("You have selected Dinner.")
        dinner()
    else:
        print("Invalid choice. Please try again.")
        menu()

# select breakfast/lunch/dinner
def breakfast():
    print("Please select the type of cuisine for Breakfast:")
   
    cuisines_bf = ["Continental", "Indian", "Chinese", "American"]
   
    for i,cuisine in enumerate(cuisines_bf):
        print(f"{i+1}. {cuisine}")
    
    choice = input("Enter your choice ((1/2/3/4)): ")

    if choice == '1':
        print("You have selected Continental Breakfast.")
    elif choice == '2':
        print("You have selected Indian Breakfast.")
    elif choice == '3':
        print("You have selected Chinese Breakfast.")
    elif choice == '4':
        print("You have selected American Breakfast.")
    else:
        print("Invalid choice. Please try again.")
        breakfast()

    
def lunch():

    print("Please select the type of cuisine for Lunch:")
    
    cuisines_lunch = ["Continental", "Indian", "Chinese", "American"]
    
    for i,cuisine in enumerate(cuisines_lunch):
        print(f"{i+1}. {cuisine}")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("You have selected Continental Lunch.")
    elif choice == '2':
        print("You have selected Indian Lunch.")
    elif choice == '3':
        print("You have selected Chinese Lunch.")
    elif choice == '4':
        print("You have selected American Lunch.")
    else:
        print("Invalid choice. Please try again.")
        lunch()

def dinner():
    print("Please select the type of cuisine for Dinner:")

    cuisines_dinner = ["Continental", "Indian", "Chinese", "American"]

    for i,cuisine in enumerate(cuisines_dinner):
        print(f"{i+1}. {cuisine}")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("You have selected Continental Dinner.")
    elif choice == '2':
        print("You have selected Indian Dinner.")
    elif choice == '3':
        print("You have selected Chinese Dinner.")
    elif choice == '4':
        print("You have selected American Dinner.")
    else:
        print("Invalid choice. Please try again.")
        dinner()

menu()


# select type of food within breakfast/lunch/dinner based on continent wise classification

