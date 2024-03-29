"""

Author: Mike Farad
RegNo: P15/102164/2017
Date: 15th November 2019, Friday

A simple helper script that contains general functions that can be re-used
elsewhere

This file can be imported as a module and contains the following
functions:

   * print_lists - A helper function that prints a nicely formatted version of
        the list to the terminal.
"""


def print_list(my_list):
    """Simply formats and prints the sorted list to the console.

        Parameters
        -----------
        my_list : list
            List to be sorted using merge sort

    """
    for element in my_list:
        print(element, end=" ")
    print()
