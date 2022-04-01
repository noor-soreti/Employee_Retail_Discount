# Noor Said - 101358069
# Lab Professor - Ms. Laily Ajellu
from function import *

# Define Menu Items
menu_options = {"1. Create Employee": 1, "2. Create Item": 2, "3. Make Purchase": 3, "4. All Employee Summary": 4,
                "5. Exit": 5}

# Program logic starts here:
end_program = False

# Create files with headers (if not exist)
write_employee()
write_item()

while not end_program:
    # Display menu options
    print("    ------------------------------- Menu -------------------------------")
    display_menu(menu_options)
    # Retrieve user input and validate
    user_option = input("Enter here: ")
    if (not user_option.isnumeric()) or (int(user_option) not in range(1, 6)):
        print("Please enter a valid number between 1 and 5")
    else:
        user_option = int(user_option)
        if user_option == 1:
            # Run function to add new employee
            print("    --------------------------- Add Employee ---------------------------")
            create_employee()
        elif user_option == 2:
            # Run function to add new item
            print("    ----------------------------- Add Item -----------------------------")
            create_item()
        elif user_option == 3:
            # Run function to make purchase
            print("    --------------------------- Make Purchase ---------------------------")
            purchase_page()
        elif user_option == 4:
            # Run function to view employee summary
            print("    -------------------------- Employee Summary ------------------------")
            employee_summary()
        elif user_option == 5:
            # Quit Program
            print("    ----------------------------- Quiting -----------------------------")
            print("Exiting...")
            end_program = True
    # Function call to return to menu or quit the program
    end_program = quit_program(end_program)