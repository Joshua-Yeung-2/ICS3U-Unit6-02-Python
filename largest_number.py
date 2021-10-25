# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the largest of random number

import random


def largest_number(random_number):
    # this function is to calculate the average of random number
    largest = 0

    # process
    for loop_counter in range(1, len(random_number)):
        print(
            "The random number {0} is: {1}".format(
                loop_counter, random_number[loop_counter]
            )
        )

        if random_number[loop_counter] > largest:
            largest = random_number[loop_counter]

    return largest


def main():
    # this function is to generater a random number
    random_number = []

    # process
    print("starting ...")
    print("")

    for loop_counter in range(0, 11):
        some_variable = random.randint(1, 100)
        random_number.append(some_variable)

    # call function
    largest_number_2 = largest_number(random_number)

    print("\nThe largest number is {}".format(largest_number_2))

    print("\nDone")


if __name__ == "__main__":
    main()
