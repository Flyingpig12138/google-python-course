#!/usr/bin/env python3

import sys

def main():
    time_hour = int(input("Enter the current time in hours: "))
    mood      = input("Enter your mood now: ")

    if time_hour >= 0 and time_hour <= 24:
        print('drink recommendation: ')
        if mood == 'sleepy':
            if time_hour < 12:
                print('coffee')
            else:
                print('water')
        elif mood == 'thirsty':
            if time_hour > 7:
                print('water')
            else:
                print('still sleeping')
        elif not mood == 'normal': 
            print('you siao liao')
    else: 
        print('warning: time input is wrong')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()


