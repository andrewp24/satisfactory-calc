"""
This file will be used for calculating the resources needed. It will also call a separate file
that basically serves as a lookup file.. most likely held in a dict
"""


def calc_needs(item, num_of_item):
    if num_of_item > 1:
        print(f"Calculating what materials are needed to create {num_of_item} {item}s")
    else:
        print(f"Calculating what materials are needed to create {num_of_item} {item}")


