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
    
def lambda_test() :
    print("Lambda test: ")
    print("Print operators defined in for_import.lambda_test()")
    print("Lambda set to L_TEST variable (L_TEST = lambda : lambda_test()) ")
    print("And passed to another function as parameter")
    
L_TEST = lambda : lambda_test()

def lambda_executor_function(lambda_function) :
    lambda_function()    
