grocerylist = []

while True:
    print("\nOptions: add / remove / show / exit")
    action = input("What would you like to do? ")

    if action == "add":
        item = input("Enter item to add: ")
        grocerylist.append(item)
        print(f"{item} added.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in grocerylist:
            grocerylist.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif action == "show":
        print("Your grocery list:")
        for i in grocerylist:
            print("-", i)

    elif action == "exit":
        break

    else:
        print("Invalid option.");