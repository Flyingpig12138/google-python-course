#!/usr/bin/env python3

# practice examples listed in [python strings] section


import sys

def strings_methods(s):
    # lower() / upper()
    print('Lower case: ', s.lower())
    print('Upper case: ', s.upper())

    # strip
    print('White space removed (strip): ', s.strip())

    # isalpha/isdigit/isalnum
    print('isalpha: ', s.isalpha())  # True if all characters in the string are alphabetic
    print('isdigit: ', s.isdigit())  # True if all characters in the string are digits
    print('isalnum: ', s.isalnum())  # Trut if all characters in the string are alphanumeric

def string_slices(s):
    print('----- string slices and index-ed access -----')
    print('The input string is: ', s)
    print('s[1:4] is: \t', s[1:4])
    print('s[1:] is: \t', s[1:])
    print('s[:] is: \t', s[:])
    print('s[1:100] is: \t', s[1:100], ' Wow there is no overflow')
    print('s[0:] is: \t', s[0:])
    print('s[-1] is: \t', s[-1])
    print('s[-2] is: \t', s[-2])
    print('s[:-3] is: \t', s[:-3])  # going from the first char to char -3
    print('s[-3:] is: \t', s[-3:])  # going from char -3 to the end of string

def string_formatting(value):
    print('----- string formatting and f-string -----')
    # example 1
    print('The value of pi is: ', value)
    print(f'the value of pi is {value:.3f}')
    # example 2
    brand = 'honda'
    model = 'CB400SF'
    cylinder = 4
    year = 2019
    print(f'My motorcycle is a {brand} {model}. It is manufactured in {year} and has {cylinder} cylinders. (printed using f-string)')
    print('My motorcycle is a %s %s. It is manufactured in %d and has %d cylinders. (printed using %% operator)' % (brand, model, year, cylinder))
    # example 3
    address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
                    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
                    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]
    for person in address_book:
        print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')



def main():
    # immutable string
    s1 = 'hello'
    s2 = 'flyingpig12138'
    s3 = s1 + s2
    print(s3*3)

    # access character
    s4 = 'flyingpig12138'
    print(s1[3]) # should show i

    # convert to string using str()
    pi = 3.1415926
    print('The value of pi is: ' + str(pi))

    # math operations
    print(10//3) # use // for integer division

    # backslash and raw string
    """
    backslash is treated literally and not as an escape character in raw string
    """
    s5 = r'\n\n\t\walao'
    s6 = '\n\n\t\walao'
    print(s5, s6)

    # multi line
    multi = """ To be,
    or not to be, 
    that is the question."""
    print(multi)

    # string methods
    s7 = 'FlyingPig12138'
    strings_methods(s7)

    # string slices
    s8 = 'honda'
    string_slices(s8)

    # string formatting
    value = 3.1415
    string_formatting(value)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()



