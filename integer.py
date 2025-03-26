#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 25, 2025
# This program tells the user if
# their number is positive, negative
# or zero


def main():
    # get the user's number
    user_num = int(input("Enter your number: "))

    # check if the number is positive, negative or zero
    if user_num == 0:
        print("Your number is 0")
    elif user_num > 0:
        print("Your number is positive")
    else:
        print("Your number is negative")


if __name__ == "__main__":
    main()
