# grocery item class with name and quantity attributes
class GroceryItems:
    name = ""
    quantity = 0
    price = 0.0


def main():
    # counter i to keep track of total number of items
    i = 0
    # a list objects
    item_list = []
    print("Try help to see more options : ")
    # infinite loop to keep the program running
    while True:
        # default input to chose operation
        inpt = input("> ")
        # help displays all the available options
        if inpt.lower() == "help":
            print("Choose and enter the operation from below : ")
            print("Add -> Add an item ")
            print("Edit -> Edit an item quantity ")
            print("Remove -> Remove an item ")
            print("View -> View the inventory ")
        # add adds new item
        elif inpt.lower() == "add":
            item_list.append(i + 1)
            item_list[i] = GroceryItems()
            item_list[i].name = input("Enter the name for the item : ")
            # using try and except for ValueError
            try:
                item_list[i].quantity = int(input("Enter the quantity of the item : "))
                item_list[i].price = float(input("Enter the price of the item : "))
                print("Item added successfully")
            except ValueError:
                print("Please enter a valid number!")
            # increasing item count
            i = i + 1
        # edit edits teh quantity of already listed item
        elif inpt.lower() == "edit":
            inpt = input("Enter the name of the item : ")
            # boolean variable to check if item to be edited is present in the item list, if not throw an error
            item_present = False
            # following loop searches for the item by name
            for iterator in range(0, i, 1):
                if inpt.lower() == item_list[iterator].name:
                    item_present = True
                    # shows options to edit the quantity of item
                    print("Choose from the following modes : ")
                    print("Set -> Set quantity of teh stock ")
                    print("Add -> Add to stock ")
                    print("Reduce -> Reduce from stock ")
                    inpt = input("> ")
                    # using try and except for ValueError
                    try:
                        # adding to the stock
                        if inpt.lower() == "add":
                            item_list[iterator].quantity = item_list[iterator].quantity + int(input("Enter the quantity to be added: "))
                        # removing from the stock
                        elif inpt.lower() == "reduce":
                            item_list[iterator].quantity = item_list[iterator].quantity - int(input("Enter the quantity to be reduced: "))
                        # setting the stock value to a number
                        elif inpt.lower() == "set":
                            item_list[iterator].quantity = int(input("Enter the new quantity of the item : "))
                        # default case
                        else:
                            print("Invalid input, please enter again! ")
                    except ValueError:
                        print("Please enter a valid number!")
                    break
            # checks if the above block of code got executed
            if item_present == False:
                print("item not present in the list, try again.")
        # remove removes a specific item
        elif inpt.lower() == "remove":
            # checks if item list is empty
            if len(item_list) == 0:
                print("Nothing to remove here! Shelves are empty.")
            else:
                inpt = input("Enter the name of the item : ")
                # following loop searches for the item by name and removes it
                for iterator in range(0, i, 1):
                    if inpt.lower() == item_list[iterator].name:
                        del item_list[iterator]
                        print("Item removed successfully")
                        # reducing item count
                        i = i - 1
                        break
        # view shows the inventory
        elif inpt.lower() == "view":
            # checks if item list is empty or not
            if len(item_list) == 0:
                print("Nothing to show here! Shelves are empty.")
            else:
                #      <----20-spaces-----><----20-spaces----->
                print("Item Name           Quantity            Price(INR)")
                # following loop prints each element in item_list
                for iterator in range(0, i, 1):
                    # counts the number of spaces to be printed after name
                    space_cnt1 = 20 - len(item_list[iterator].name)
                    # counts the number of spaces to be printed after quantity
                    space_cnt2 = 20 - len(str(item_list[iterator].quantity))
                    print('%s%s%d%s%.2f' % (item_list[iterator].name, " " * space_cnt1, item_list[iterator].quantity, " " * space_cnt2, item_list[iterator].price))
        # default case
        else:
            print("Please enter a valid input. Try 'help' for more options. ")


# main function call
if __name__ == "__main__":
    main()
