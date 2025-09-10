# practice examples listed in [python strings] section

import sys

def main():
    # immutable strings
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


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()



