import csv

item_file_name = 'item_list.csv'
item_fieldnames = ['Item_Number', 'Item Name', 'Item Cost']

def unique_item(column, el):
    with open(item_file_name, 'r+') as my_file:
        reader = csv.DictReader(my_file)
        for row in reader:
            if row[column] == el:
                return 2
    return -1

if unique_item('Item_Number', '3') == -1:
    print("-1")
else:
    print("not")