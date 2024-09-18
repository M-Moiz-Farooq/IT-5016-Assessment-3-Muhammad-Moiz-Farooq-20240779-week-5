'''
Week 5 Lab using def

Author: Muhammad Moiz Farooq-20240779
Whitecliffe College, AKL

'''
def collect_user_data():
    idcounter = 5000
    uniqueidcount = idcounter + 1
    idcounts = []

    while True:
        name = input("Enter your name (type 'done' to exit): ")
        if name.lower() == 'done':
            break

        age = input(f"Hi {name}! Enter your age: ")
        email = input(f"Could you please enter your email too {name}:? ")

        print(f"Hi {name}! Your unique ID is: {uniqueidcount}")
        idcounts.append((name, uniqueidcount))  # Store as a tuple instead of a string
        uniqueidcount += 1

    print("List of unique IDs created against names inputted is:")
    for name, uniqueid in idcounts:
        print(f"{name}: {uniqueid}")

def shopping_list():
    total = 0
    shoppinglist = []

    while True:
        item = input("Enter name of item (or type 'done' to finish): ")
        item = item.lower()
        if item == 'done':
            break

        price = float(input(f"Enter price of {item}: "))
        shoppinglist.append((item, price))  # Store as a tuple instead of a string
        total += price

    print("Your shopping list:")
    for item, price in shoppinglist:
        print(f"{item}: ${price:.2f}")

    print(f"Your total is: ${total:.2f}")

    if total < 150:
        print("Category: Low")
        print("Proceed with standard routine")
    else:
        print("Category: High")
        print("Review for potential discount")

# Call the functions
collect_user_data()
shopping_list()