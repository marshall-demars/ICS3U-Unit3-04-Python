#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program uses if statements to decipher positive and negative numbers
#    with user input


def main():
    # this uses if statements to guess a random number

    # input
    user_integer = int(input("Enter any number: "))

    # process and output
    if user_integer > 0:
        print("\nYou chose a positive number!")
    elif user_integer < 0:
        print("\nYou chose a negative number!")
    elif user_integer == 0:
        print("\nYou chose a neutral number!")
    else:
        print("\nI don't know what your number is.")

    print("\nDone.")


if __name__ == "__main__":
    main()
