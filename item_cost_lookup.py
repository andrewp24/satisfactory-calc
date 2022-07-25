"""
This file will do extractions from a csv which holds items and their resource cost
schema should be:
NOTE: -1s are used if the value doesn't exist. for example, if an item only has one pre req material,
then it will have -1s in the following pre req material

csv header notes:
item_id:                a unique id for each item
item_name:              the english name for the item in the game
num_diff_pre_req_need:  the amount of different types of materials needed to craft
pre_req_need_id_1:      the id of the first pre req material (allows link to data for that item)
need_amount_1:          the amount of the first item that is needed
pre_req_need_id_2:      the id of the second pre req material (allows link to data for that item)
need_amount_2:          the amount of the first item that is needed
pre_req_need_id_3:      the id of the third pre req material (allows link to data for that item)
need_amount_3:          the amount of the first item that is needed

"""

import csv


def read_csv(item_name):  # add parameters for this to change based on the searched item name
    item_found = False
    with open('data/item_cost.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if item_name == row[1]:
                item_found = True
                searched_row = row
                break
        if item_found:
            print(searched_row)
            analyze_finding(searched_row)
        else:
            print(f'The item you were looking for: {item_name} could not be found. Check the spelling and run the '
                  f'program again.')


def analyze_finding(searched_row):
    print(f'item id: {searched_row[1]}\n'
          f'item name: {searched_row[2]}\n'
          f'number of other items needed: {searched_row[3]}\n'
          f'pre req item id: {searched_row[4]}\n'
          f'pre req num needed: {searched_row[5]}\n'
          f'pre req item id: {searched_row[6]}\n'
          f'pre req num needed: {searched_row[7]}\n')
