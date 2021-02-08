#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a=int(len(arr))
    for x in range(len(arr)):
        if arr[x]>0:
            z=arr[x]/a
            print(float(round(z,6)))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
