#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program tells user if a given year is a leap year

import random
import string


def main():
    # This function determines whether or not it is a leap year

    # Input
    year_as_string = str(input("Enter the year: "))

    # Process and Output
    try:
        year_as_integer = int(year_as_string)
        if year_as_integer % 4 == 0:
            if year_as_integer % 100 == 0:
                if year_as_integer % 400 == 0:
                    print("\nIt is a leap year!")
                else:
                    print("\nIt is a common year!")
            else:
                print("\nIt is a leap year!")
        else:
            print("\nIt is a common year!")
    except Exception:
        print("\n{} is not a valid year!".format(year_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
