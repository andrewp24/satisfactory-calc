"""
This file will hold all user input code
"""


def what_item():
    item = input("What item do you need to make? ")
    item = item.strip().lower().replace(" ", "_")
    if item == "":
        print("This cannot be empty. please type in a craftable item from the game.")
        item = what_item()
    return item


def how_many():

    try:
        amount = int(input("How many of those do you need to make? "))
    except ValueError:
        print("Not a valid value for the amount. Must be type int")
        amount = how_many()
    return amount
