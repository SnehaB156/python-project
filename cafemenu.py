menu={
'Espresso': 50,
'Macchiato':60,
'Breve':60,
'Mocha':70,
'Cappuccino':75,

'Daily Dark Roast': 80,
'Pour Over':75,
'Hot Chocolate':80,

'Bagel':90,
'Muffin':75,
'Breakfast Sandwich':100,
'Croissant':100,
'Breakfast Burrito':120,

'Iced Coffee':80,
'Iced Mocha':100,
}

#Greeting
print("Welcome to codecafe")
print("Espresso: Rs50\nMacchiato:60\nBreve:60\nMocha:70\nCappuccino:75\n\nDaily Dark Roast: 80\nPour Over:75\nHot Chocolate:80\n\nBagel:90\nMuffin:75\nBreakfast Sandwich:100\nCroissant:100\nBreakfast Burrito:120\n\nIced Coffee:80\nIced Mocha:100")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaialable in menu")

another_order = input("Do you want to something else?(Yes/No)")
if another_order == "Yes":
    item_2 =input ("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable in menu")
print(f"The total amount of items is {order_total}")       