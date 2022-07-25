# This program is going to be asking the user what items they want to produce and them

import user_input
import calculations


if __name__ == "__main__":

    item = user_input.what_item()
    num_of_item = user_input.how_many()

    res = calculations.calc_needs(item, num_of_item)
