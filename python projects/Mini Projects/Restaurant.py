# # define the menu of restaurant
menu ={
    'pizza':40,
    'pasta':50,
    'burger':70,
    'coffee':100,
}

print("Welcome, Menu below")
print("Pizza: Rs40\nBurger: Rs70\nPasta: Rs50\nCoffee: Rs100\n")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item{item_1} is not available")

another_order = input("Do you want to add another item? (Yes/no)")
if another_order =="yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items is {order_total}")
