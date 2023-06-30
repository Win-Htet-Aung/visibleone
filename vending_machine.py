import os
import time

items = [
    {"name": "Coca Cola", "price": 3.35},
    {"name": "Pepsi", "price": 2.1},
    {"name": "Orange", "price": 2.85},
]

avail_money = [5, 10, 15, 20]
money_left = 0
stage = 1

def display_menu():
    os.system("clear")
    width = 36
    deco = "+" * width
    header_format = f"|{{:^{width-2}}}|"
    item_format = f"[{{}}] {{:{width-11}}}{{:5.2f}} $"
    print(deco)
    print(header_format.format("Welcome to Vending Machine"))
    print(deco)
    for i, item in enumerate(items):
        print(item_format.format(i+1, item["name"], item["price"]))
    print(deco)
    print(f"Money Left : {money_left:.2f} $")

def get_money():
    money_str = "{}$"
    for i in range(len(avail_money) - 1):
        money_str = ", ".join((money_str, "{}$"))
    prompt_format = f"Insert Money ({money_str}) : "
    while 1:
        try:
            money = int(input(prompt_format.format(*avail_money)))
            if money not in avail_money:
                raise ValueError
        except ValueError as e:
            print("Input must be one of :", avail_money)
        else:
            return money
        
def get_item():
    item_numbers = "{}"
    for i in range(len(items) - 1):
        item_numbers = ", ".join((item_numbers, "{}"))
    prompt_format = f"Select an item number ({item_numbers}) : "
    while 1:
        try:
            item = int(input(prompt_format.format(*(list(range(1, len(items) + 1))))))
            if item not in range(1, len(items) + 1):
                raise ValueError
        except ValueError as e:
            print("Input must be one of :", list(range(1, len(items) + 1)))
        else:
            return item

while True:
    display_menu()
    if stage == 1:
        money_left += get_money()
        display_menu()
        resp = input("Do you want to insert more money? (y/n) : ").lower()
        if resp == "y":
            continue
        stage = 2
    elif stage == 2:
        item = get_item()
        if items[item-1]["price"] <= money_left:
            money_left -= items[item-1]["price"]
            display_menu()
            print(f"Purchased {items[item-1]['name']}")
        else:
            print("Money left is not enough!")
            time.sleep(1)
            stage = 1
            continue
        resp = input("Do you want to buy more drinks? (y/n) : ").lower()
        if resp == "y":
            continue
        print("Good Bye!")
        break
    