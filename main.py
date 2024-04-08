# import the required modules
import random # for randomly selecting the dealers
# Welcome message for the user when the program start
print("\t\t!WELCOME TO ONE NET CAFE!")
# create list
items = []
# function to display menu
def menu():
    print("\t\t\t...OPTIONS...")
    # Display menu option for the user to select
    print("Type |AID| for adding item details.")
    print("Type |DID| for delete item details.")
    print("Type |UID| for update item details.")
    print("Type |VID| for viewing item details.")
    print("Type |SID| for saving the item details to the text file.")
    print("Type |SDD| for selecting four dealers randomly from a file.")
    print("Type |VRL| for displaying all the detail of the randomly selected dealers.")
    print("Type |LDI| for display the items of the given dealer.")
    print("Type |ESC| for exit the program.")
    # prompt user to enter their choice
    choice = input("\nWhat is your Choice: ")

    # If the user enters 'AID', add a new item
    if choice.upper() == "AID":
        add_item()
        while True:
            answer = input("Do you want to add another item? [Yes/No]: ")
            if answer.upper() == "YES":
                add_item()
            elif answer.upper() == "NO":
                menu()
                break
    # If the user enters 'DID', delete the items of a given dealer
    elif choice.upper() == "DID":
        delete_item()
    # If the user enters 'UID', update the details of an item
    elif choice.upper() == "UID":
        update_item()
    # If the user enters 'VID', view all items
    elif choice.upper() == "VID":
        view_items()
    # If the user enters 'SID', save the items to a text file
    elif choice.upper() == "SID":
        save_to_file(items)
    # If the user enters 'SDD', randomly select four dealers
    elif choice.upper() == "SDD":
        random_dealers()
    # If the user enters 'VRL', view all the details of the randomly selected dealers
    elif choice.upper() == "VRL":
        view_selected_dealers()
    # If the user enters 'LDI', display the items of a given dealer
    elif choice.upper() == "LDI":
        display_items_of_dealer()
    # If the user enters 'ESC', exit the program
    elif choice.upper() == "ESC":
        print("\nThank for using 'ONE NET CAFE'")
        exit()
    else:
        # If the user enters an invalid choice, display an error message
        print("Invalid option.")
        menu()

#define a function add a new item
def add_item():
    while True:
        try:
            # Prompt user to enter the item,name and brand
            item_code = int(input("Enter item code: "))
            item_name = input("Enter item name: ")
            item_brand = input("Enter item brand: ")

            while True:
                try:
                    # Enter item price and handle invalid input
                    item_price = float(input("Enter item price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid input.")

            while True:
                try:
                    # Enter item quantity and handle invalid input
                    item_quantity = int(input("Enter item quantity: "))
                    break
                except ValueError:
                    print("Invalid Input. Please Try again.")

            item_category = input("Enter item category: ")
            purchased_date = str(input("Enter purchased date (YYYY/MM/DD): "))
            # create a dictionary for the item and append it to the items list
            item = {"code": item_code, "name": item_name, "brand": item_brand, "price": item_price,
                    "quantity": item_quantity, "category": item_category, "purchased_date": purchased_date}
            items.append(item)

            print("Item added Successfully")
            break
        except ValueError:
            print("\nInvalid input. Try again.\n")


# Define a function to delete the items of a given dealer
def delete_item():
    # prompt user to enter the item code for delete
    item_code = int(input("Enter item code to delete:"))
    for item in items:
        if item["code"] == item_code:
            items.remove(item)
            print("Item deleted successfully!")
            menu()
            break
    else:
        print("Item code {} not found".format(item_code))
        delete_item()
        menu()

# Define a function to update the details of an item
def update_item():
    # prompt user to enter the item code for update
    item_code = int(input("Enter the item code you want to update: "))
    for item in items:
        if item["code"] == item_code:
            item_name = input(f"Enter the new name: ")
            item_brand = input(f"Enter the new brand: ")
            while True:
                try:
                    item_price = float(input(f"Enter the new price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid input.")
            while True:
                try:
                    item_quantity = int(input(f"Enter the new quantity: "))
                    break
                except ValueError:
                    print("Invalid Input. Please Try again.")
            item_category = input(f"Enter the new category: ")
            purchased_date = input(f"Enter the new purchased date (YYYY/MM/DD): ")
            item["name"] = item_name
            item["brand"] = item_brand
            item["price"] = item_price
            item["quantity"] = item_quantity
            item["category"] = item_category
            item["purchased_date"] = purchased_date
            print("Item updated successfully.")

            menu()
            break
    else:
        print("Item not found.")
        update_item()

# For creating a formatted table from data
from tabulate import tabulate

# Define a function to view all items
def view_items():
    headers = ["Code", "Name", "Brand", "Price", "Quantity", "Category", "Purchased Date"]
    sorted_items = sorted(items, key=lambda x: x["code"])
    rows = [[item["code"], item["name"], item["brand"], item["price"], item["quantity"], item["category"], item["purchased_date"]] for item in sorted_items]
    print(tabulate(rows, headers=headers, tablefmt="simple_grid", numalign="right"))

    #calculate the total
    total = sum([item["price"] * item["quantity"] for item in items])
    print("Total: Rs:",total)
    menu()

# Define a function to save the items to a text file
def save_to_file(items):
    print("Saving item details to file..\n")
    with open('data.txt', 'w') as f:
        f.write(str(items))
        f.close()
    print("Item saved successfully!")
    menu()

# Define a function to randomly select four dealers
def random_dealers():
    with open("dealers.txt", "r") as f:
        lines = f.readlines()
        random_dealers = []
        while len(random_dealers) < 4:
            dealer = random.choice(lines).strip()
            dealer1 = dealer.split(",")[0]

            if dealer1 not in random_dealers:  # check for duplicates
                random_dealers.append(dealer1)
                print(dealer1)
        print("\n4 dealers are selected randomly!")

        return random_dealers
menu()

# Define a function to randomly select four dealers and display their details
def view_selected_dealers():
    # Get 4 random dealers
    random_dealers_list = random_dealers()

    # Read dealers from file
    with open('dealers.txt', 'r') as file:
        dealers = file.readlines()

    # Filter dealers by name
    filtered_dealers = [dealer for dealer in dealers if dealer.split(',')[0] in random_dealers_list]

    # Sort dealers by location
    n = len(filtered_dealers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            loc1, name1 = filtered_dealers[j].split(',')[2], filtered_dealers[j].split(',')[0]
            loc2, name2 = filtered_dealers[j + 1].split(',')[2], filtered_dealers[j + 1].split(',')[0]
            if loc1 > loc2 or (loc1 == loc2 and name1 > name2):
                filtered_dealers[j], filtered_dealers[j + 1] = filtered_dealers[j + 1], filtered_dealers[j]
    # Display details of each dealer
    for dealer in filtered_dealers:
        details = dealer.split(',')
        print('Dealer Name:', details[0])
        print('Contact Number:', details[1])
        print('Location:', details[2])
        print()
        menu()

menu()

def display_items_of_dealer():
    # Prompt for a dealer name
    dealer_name = input("Enter dealer name: ")

    # Read dealer details from file
    with open('dealers.txt', 'r') as dealer_file:
        dealer_lines = dealer_file.readlines()

    # Find the dealer's details
    dealer_location = None
    for line in dealer_lines:
        details = line.strip().split(',')
        if details[0] == dealer_name:
            dealer_location = details[2]
            break

    # If dealer is found, display their items
    if dealer_location:
        # Read item details from file
        with open('items.txt', 'r') as item_file:
            item_lines = item_file.readlines()

        # Find items sold by the dealer
        dealer_items = []
        for line in item_lines:
            details = line.strip().split(',')
            if details[2] == dealer_location:
                dealer_items.append(details[0])

        # Display the dealer's items
        print(f"{dealer_name} sells the following items:")
        for item in dealer_items:
            print(item)
    else:
        print(f"Dealer {dealer_name} not found in the file.")

    menu()
menu()