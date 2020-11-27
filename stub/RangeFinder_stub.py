#! /usr/bin/env python3

#
# file name: tof_code_v1
# Description: RangeFinder functional code
# Author(s): Sunjeevani Pujari 
#
import time
import sys 
class RangeFinder:
    
    def __init__(self):
        # Get initial range from file
        try:
            with open("initial_range.txt", "r") as range_file:
                self.range = range_file.read().strip()
        except FileNotFoundError as e:
            print("Could not open testcase files.")
            exit(1)

    def get_range(self):
        distance = int(self.range)
        print(distance)
        return distance
if __name__ == "__main__":
    range_finder = RangeFinder()
    range_finder.get_range()