#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the greater number


def main():

    while True:
        # imput
        first_number = input("Input a number:")
        second_number = input("Input another number:")

        # process
        try:
            first_number_as_number = int(first_number)
            second_number_as_number = int(second_number)
            if first_number_as_number > second_number_as_number:
                # output
                print("{0} is the greater number"
                      .format(first_number_as_number))
                break
            elif second_number_as_number > first_number_as_number:
                print("{0} is the greater number"
                      .format(second_number_as_number))
                break
            else:
                print("Numbers are equal")
                break
        except(ValueError):
            print("Not a valid number inputted")
        finally:
            print("")


if __name__ == "__main__":
    main()
