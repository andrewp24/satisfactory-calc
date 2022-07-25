"""
This file will hold all user input code
"""


def what_item():
    item_name = input("What item do you need to make? ")
    item_name = item_name.strip().lower().replace(" ", "_")
    if item_name == "":
        print("This cannot be empty. please type in a craftable item from the game.")
        item_name = what_item()
    return item_name


def how_many():

    try:
        amount = int(input("How many of those do you need to make? "))
    except ValueError:
        print("Not a valid value for the amount. Must be type int")
        amount = how_many()
    return amount
