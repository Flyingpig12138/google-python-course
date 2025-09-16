#! /usr/bin/env python3
import sys

def main():
    # build up a dictionary
    dict = {}
    dict['Honda'] = 'CB400SF'
    dict['Yamaha'] = 'XSR155'
    dict['Kawasaki'] = 'Z900RS'
    dict['Suzuki'] = 'hayabusa'
    print(dict)

    # loop up 
    print(dict['Kawasaki'])

    # mutable 
    dict['Suzuki'] = 'DRZ400'  # modify a key value
    print(dict)
    dict['Triumph'] = 'daytona660'
    print(dict)

    # check if key is in dict
    if 'BMW' in dict:
        print('Wow I got a BMW')
    else: 
        print('It is pronounced as BMV')

    # for loop: iterates on keys
    for key in dict:
        print(key)
    print('-----')

    # dict.keys(): list all keys in dict
    print(dict.keys())
    print(type(dict.keys()))  # <class 'dict_keys'>

    # dict.values(): lista ll values in dict
    print(dict.values())
    print(type(dict.values()))  # <class 'dict_values'>

    print('-----')
    
    # combine with sorted function (operate on keys also)
    dict_sorted = sorted(dict, key=len)
    for key in dict_sorted:
        print(key)
    print('-----')
    # alternatively
    for key in sorted(dict, key=len):
        print(key, dict[key])

    # items(): return all key-value as tuples
    print(dict.items())
    print(type(dict.items()))  # <class 'dict_items'>

    # looping through all items in dict
    for (key, value) in dict.items():
        print(f'I have a {key} bike with model {value}')

    # dict formatting using %
    print('I have a %(Honda)s and my next dream bike is %(Kawasaki)s' % dict) 

    # del operation (deletion)
    var = 12138 
    del var  # var no more!

    list = [1,2,3,4,5]
    del list[1]
    print(list)  # [1,3,4,5]

    del dict['Triumph']
    print(dict)









# standard boilerplate
if __name__ == "__main__":
    main()
