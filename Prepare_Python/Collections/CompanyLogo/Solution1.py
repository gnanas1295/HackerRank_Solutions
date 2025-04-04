#!/bin/python3

import math
import os
import random
import re
import sys

from operator import itemgetter

if __name__ == '__main__':
    s = input()
    
    final_dict = {}
    final_list = []
    
    for char in sorted(s):
        if char not in final_dict.keys():
            final_dict[char] = 1
        else:
            final_dict[char] += 1
    final_dict_list = list(final_dict.items())
    
    count = 0
    for k, v in sorted(final_dict.items(), key = itemgetter(1), reverse = True):
        count += 1
        if count <= 3:
            print(k, v)