"""
Some very simple program to start with.
Here we have map (dictionary) of commands shortcuts and descriptions and
simple function that starts function from other script in this
module name.

Created by akaish at 21.03.2019
"""
from first_steps.for_import import hello as hello_uname
from first_steps.for_import import A_AND_B_EQUAL
from first_steps.for_import import A_LESS_THEN_B
from first_steps.for_import import B_LESS_THEN_A
from first_steps.for_import import compare_two_integers as compare 

command_dictionary = {
    '-h' : 'help',
    '-p1' : 'hello username program',
    '-p2' : 'compare two integers',
    '-q' : 'quit'}

def input_integer(input_string) :
    integer_str = input(input_string)
    if(integer_str == 'q') : return None
    try :
        return int(integer_str)
    except ValueError :
        print("Input something that can be parsed to integer with base 10 or print 'q' to stop!")
        input_integer(input_string)
    
def exit_from_p2() :
    print("Quit program -p2!")
    main()

LESS_TNAN = "is less than"
GREATER_TNAN = "is greater than"
EQUEAL = "is equal to"
PATTERN = "{0} {1} {2}!"

def switch_alike_with_lamdas_for_p2(x, a, b):
    return {
        A_AND_B_EQUAL : lambda a, b : PATTERN.format(a, EQUEAL, b),
        A_LESS_THEN_B : lambda a, b : PATTERN.format(a, LESS_TNAN, b),
        B_LESS_THEN_A : lambda a, b : PATTERN.format(a, GREATER_TNAN, b),  
        }[x](a, b)

def main() :
    command = input("Insert command name (-h for command list): ")
    if(command == '-h') :
        for command_key in command_dictionary.keys() :
            print("Input {0} for run {1}".format(command_key, command_dictionary.get(command_key)))
        main()
    elif(command == '-p1') :
        hello_uname()
        main()
    elif(command == '-p2') :
        a = input_integer("Input first value to compare : ")
        if(a == None): exit_from_p2()
        b = input_integer("Input second value to compare :")
        if(b == None) : exit_from_p2()
        print(switch_alike_with_lamdas_for_p2(compare(a, b), a, b))
        main()
    elif(command == '-q') :
        print("Bye bye!")
        return
    else :
        print("Unknown command, enter -h for available commands!")
        main()
        
        
main()
        
    
    