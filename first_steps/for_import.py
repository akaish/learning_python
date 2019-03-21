"""
Few functions for first program

Created by akaish at 21.03.2019
"""

def hello():
    username = input("What's your name, friend? :")
    print('Hello, {0}!'.format(username))
    

A_LESS_THEN_B = 1
B_LESS_THEN_A = 2
A_AND_B_EQUAL = 3

def compare_two_integers(a, b):
    if a > b :
        return B_LESS_THEN_A
    elif a < b :
        return A_LESS_THEN_B
    else :
        return A_AND_B_EQUAL
