#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    gmail_list = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if emailID.endswith("@gmail.com"):
            gmail_list.append({'first_name': firstName, 'email': emailID})

    sorted_list = sorted(gmail_list, key=lambda x: x['first_name'])
    for gmail in sorted_list:
        print(gmail['first_name'])
