#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    m=meal_cost
    print(m)
    tip=(m*tip_percent)/100
    print(tip)
    tax=(m*tax_percent)/100
    print(tax)
    print(round(m+tip+tax))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
