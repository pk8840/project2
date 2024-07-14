menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'veg noodles':80,
    'coffee':100,
}
print("welcome to PYTHON Restaurent")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nveg noodles: Rs80\ncoffee: Rs100")
order_total=0
item_1=input("Enter the name of item you waant to order= ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"please order something else we can serve you")
another_order = input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"order item {item_2} is not available!")
print(f"The total amount of items to pay  is {order_total}")
