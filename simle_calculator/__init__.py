"""
Second my program in Python, simple calculator (EP only).
So, it should do following thing:
* calculate inputed expressions (format = '[float_value_or_variable][whitespace][operator][whitespace][float_value_or_variable]')
* save last successful operation result to MEM variable
* support display option setting (symbols after dot)
* support of user defined variables with names [A-Z] (English alphabet)

Also, here should be binary search implementation, EP.

Created by akaish at 21.03.2019
"""
variables = {}

permitted_var_names = ('A', 'B', 'C', 'D', 'E', 'F', 'G',
                       'H', 'I', 'J', 'K', 'L', 'M', 'N',
                       'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                       'V', 'W', 'X', 'Y', 'Z')

system_variables = ('MEM', "SAD")

# TODO
def check_varname(var_name) :
    print("")

# TODO
def set_variable(var_name, var_value) :
    if(check_varname(var_name)) :
        print()
    else :
        print("") 

# TODO      
def set_system_variable(var_name, var_value) :
    print()

def command(command_name, a, b) :
    return {
        '/' : lambda a, b : a / b,
        '*' : lambda a, b : a * b,
        '+' : lambda a, b : a + b,
        '-' : lambda a, b : a - b,
        '^' : lambda a, b : a ** b,
        '=' : lambda a, b : set_variable(a, b)
        }[command_name](a, b)

# TODO
def main() :
    expression = input('Input expression or command (-h for help) :')
    
main()

    