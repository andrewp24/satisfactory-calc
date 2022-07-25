"""
This file will be used for calculating the resources needed. It will also call a separate file
that basically serves as a lookup file.. most likely held in a dict
"""
import item_cost_lookup


def calc_needs(item_name, num_of_item):
    if num_of_item > 1:
        print(f"Calculating what materials are needed to create {num_of_item} {item_name}s")
    else:
        print(f"Calculating what materials are needed to create {num_of_item} {item_name}")

    item_cost_lookup.read_csv(item_name)


