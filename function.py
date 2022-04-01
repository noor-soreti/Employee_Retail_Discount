from tabulate import tabulate
import csv

# Variable Definitions - Employees file
employee_file_name = 'employee_list.csv'
employee_fieldnames = ['ID', 'Name', 'Type', 'Years_Worked', 'Total_Purchased', 'Total_Discounts',
                       'Employee_Discount_Number']
# Variable Definitions - Items file
item_file_name = 'item_list.csv'
item_fieldnames = ['Item_Number', 'Item_Name', 'Item_Cost']


# Quit program or continue to menu
def quit_program(end_program):
    continue_add = input("\nGo back to menu? [YES/NO]")

    while continue_add.lower() not in ['yes', 'no']:
        continue_add = input("Please enter YES or NO")

    if continue_add.lower() == "no":
        end_program = True

    return end_program


# Validation: Checks if element exists employee file
def unique_employee(column, el):
    with open(employee_file_name, 'r') as my_file:
        reader = csv.DictReader(my_file)
        for row in reader:
            if row[column] == el:
                return row
    return -1


# Validation: Checks if element exists items file
def unique_item(column, el):
    lists = list()
    with open(item_file_name, 'r+') as my_file:
        reader = csv.DictReader(my_file)
        for row in reader:
            if row[column] == el:
                return list(row)
                # lists.append(list(row))
                # return lists
    return -1


# Update employee file
def update_employee_file(id, discount):
    employee_list = []
    with open(employee_file_name) as file_reader:
        reader = csv.DictReader(file_reader)
        for row in reader:
            if row['ID'] == id:
                employee_list.append([row['ID'],row['Name'],row['Type'],row['Years_Worked'],
                                      int(row['Total_Purchased']) + 1,
                                      int(row['Total_Discounts']) + discount,row['Employee_Discount_Number']])
            else:
                employee_list.append([row['ID'], row['Name'], row['Type'], row['Years_Worked'], row['Total_Purchased'],
                                      row['Total_Discounts'], row['Employee_Discount_Number']])

    # Clear file
    file_open = open(employee_file_name, 'w')
    file_open.close()
    # Popluate Headers
    write_employee()
    # Populate with rows
    for i in employee_list:
        write_employee(i)


# Displays menu
def display_menu(menu_list):
    print("Please enter the corresponding number for the action you would like to take")
    for i in menu_list:
        print(i)


# Write to employee file
def write_employee(array_val=None):
    file_open = open(employee_file_name, 'a')
    if open(employee_file_name, 'r+').readline():
        if array_val is not None:
            data = {
                'ID': array_val[0],
                'Name': array_val[1],
                'Type': array_val[2],
                'Years_Worked': array_val[3],
                'Total_Purchased': array_val[4],
                'Total_Discounts': array_val[5],
                'Employee_Discount_Number': array_val[6]
            }
            writer = csv.DictWriter(file_open, fieldnames=employee_fieldnames, lineterminator='\n')
            writer.writerow(data)
    else:
        print('Creating Employee File')
        writer = csv.DictWriter(file_open, fieldnames=employee_fieldnames, lineterminator='\n')
        writer.writeheader()
    file_open.close()


#  Write to items file
def write_item(array_val=None):
    file_open = open(item_file_name, 'a')
    if open(item_file_name, 'r+').readline():
        if array_val is not None:
            data = {
                'Item_Number': array_val[0],
                'Item_Name': array_val[1],
                'Item_Cost': array_val[2]
            }
            writer = csv.DictWriter(file_open, fieldnames=item_fieldnames, lineterminator='\n')
            writer.writerow(data)
    else:
        print('Creating Items File...')
        writer = csv.DictWriter(file_open, fieldnames=item_fieldnames, lineterminator='\n')
        writer.writeheader()
    file_open.close()


# Create new employee
def create_employee():
    add_employee = True
    # Loop: Validates user input
    while add_employee:
        print("Please fill in the following values: ")

        print("     |", end="   ")
        id = input("Employee ID: ")
        while not id.isnumeric() or (not unique_employee('ID', id) == -1):  # and NOT
            print("     |   ERROR -------> Please enter a valid (and unique) integer value")
            print("     |", end="   ")
            id = input()
        id = int(id)

        print("     |", end="   ")
        e_name = input("Employee Full Name: ")
        while not e_name.replace(" ", "").isalpha():
            print("     |   ERROR -------> Please enter a valid name")
            print("     |", end="   ")
            e_name = input()

        print("     |", end="   ")
        e_type = input("Employee Type: ")
        while e_type.lower() not in ["manager", "hourly"]:
            print("     |   ERROR -------> Please enter: Manager OR Hourly")
            print("     |", end="   ")
            e_type = input()

        print("     |", end="   ")
        y_worked = input("Years Worked: ")
        while not y_worked.isnumeric():
            print("     |   ERROR -------> Please enter an integer value")
            print("     |", end="   ")
            y_worked = input()
        y_worked = int(y_worked)

        print("     |", end="   ")
        discount_num = input("Employee Discount Number: ")
        while (not discount_num.isnumeric()) or (not unique_employee('Employee_Discount_Number', discount_num) ==-1):  # and NOT
            # EXIST
            print("     |   ERROR -------> Please enter a valid (and unique) integer value")
            print("     |", end="   ")
            discount_num = input()

        # Add new employee to list

        write_employee([id, e_name, e_type, y_worked, 0, 0, discount_num])
        # Displays updates employee table
        employee_summary()

        # Loop: user can add more employees or return to main menu
        continue_add = input("\nAdd another item? [YES/NO]")

        while continue_add.lower() not in ['yes', 'no']:
            continue_add = input("Please enter YES or NO")

        if continue_add.lower() == "no":
            add_employee = False



# Create new item
def create_item():
    add_item = True
    # Loop: Validates user input
    while add_item:
        print("Please fill in the following values: ")

        print("     |", end="   ")
        number = input("Item Number: ")
        while (not number.isnumeric()) or (not unique_item('Item_Number', number) == -1):
            print("     |   ERROR -------> Please enter a valid (and unique) numeric value")
            print("     |", end="   ")
            number = input()

        print("     |", end="   ")
        name = input("Item Name: ")
        while not name.replace(" ", "").isalpha():
            print("     |   ERROR -------> Please enter a valid item name")
            print("     |", end="   ")
            name = input()

        print("     |", end="   ")
        cost = input("Item Cost: ")
        while isinstance(cost, float):
            print("     |   ERROR -------> Please enter a numeric value")
            print("     |", end="   ")
            cost = input()

        # Add new item to list
        write_item([number, name, cost])

        # Displays updated item table
        item_summary()

        # Loop: user can add more employees or return to main menu
        continue_add = input("\nAdd another item? [YES/NO]")

        while continue_add.lower() not in ['yes', 'no']:
            continue_add = input("Please enter YES or NO")

        if continue_add.lower() == "no":
            add_item = False


# Recursive Function: Calculate discount based on number of years worked
def calculate_years_worked_discount(years_worked):
    # Base Case
    if years_worked >= 5:
        return 10
    elif years_worked == 1:
        return 2
    else:
        return 2 + calculate_years_worked_discount(years_worked-1)


# Calculates employee discount
def calculate_discount(emp):
    total_discount = calculate_years_worked_discount(int(emp['Years_Worked']))
    if int(emp['Total_Discounts']) >= 200:
        total_discount = 0
    elif emp['Type'] == 'manager':
        total_discount += 10
    else:
        total_discount += 2
    employee_id = emp['ID']
    # emp['Total_Discounts'] = int(emp['Total_Discounts']) + total_discount
    update_employee_file(employee_id, total_discount)


# Display page to make purchase
def purchase_page():
    # Variables
    # Logic Starts:
    print("Type QUIT to return to the menu...\n")
    valid_item_number = False
    valid_employee_number = False
    continue_purchase = False
    item_summary()

    while not continue_purchase:
        # Check if user wants to quit purchase
        print("     |", end="   ")
        employee_discount = input("Employee Discount Number:")
        print("     |", end="   ")
        item_number = input("Item Number:")
        if employee_discount.lower() == "quit" or item_number.lower() == "quit":
            continue_purchase = True
        elif (not employee_discount.isnumeric()) or (not item_number.isnumeric()):
            print("     |   ERROR -------> One or both values are not numeric.")
        elif (unique_employee('Employee_Discount_Number', employee_discount) == -1) or (unique_item('Item_Number', item_number) == -1):
            print("     |   ERROR -------> One or both values does not exist in current context...\n")
        else:
            emp = unique_employee('Employee_Discount_Number', employee_discount)
            item = unique_item('Item_Number', item_number)

            calculate_discount(emp)

            continue_add = input("\nMake another purchase? [YES/NO]")

            while continue_add.lower() not in ['yes', 'no']:
                continue_add = input("Please enter YES or NO")

            if continue_add.lower() == "no":
                continue_purchase = True


# Display all employees in table format
def employee_summary():
    employee_list = []
    with open(employee_file_name) as file_reader:
        reader = csv.DictReader(file_reader)
        for row in reader:
            employee_list.append([row['ID'],row['Name'],row['Type'],row['Years_Worked'],row['Total_Purchased'],
                                  row['Total_Discounts'],row['Employee_Discount_Number']])
    print(tabulate(employee_list,
                   headers=["ID", "Name", "Type", "Years Worked", "Purchased", " Discount ($)", "Discount Number"],
                   tablefmt='fancy_grid'))


# Display all items in table format
def item_summary():
    item_list = []
    with open(item_file_name, 'r+') as my_file:
        reader = csv.DictReader(my_file)
        for row in reader:
            item_list.append([row['Item_Number'], row['Item_Name'], row['Item_Cost']])
    print(tabulate(item_list, headers=["Number", "Name", "Cost"], tablefmt='fancy_grid'))
