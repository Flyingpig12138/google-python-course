#!/usr/bin/env python3

import sys

def main():
    # list
    bikes = ['CB400SF', 'XSR155', 'Z900RS']
    print(bikes[0])
    print(bikes[1])
    print(len(bikes[2]))  # length of string

    # list assignent
    my_bikes = bikes  ## Does NOT copy
    bikes.append('S1000RR')
    print(my_bikes)

    # For and In
    cc = [155, 400, 900, 1000]
    sum = 0
    for num in cc:
        sum += num
    print(sum)

    if 350 in cc:
        print('I got the CB350!')
    else: 
        print('Alright just ride super four')

    # range
    for i in range(5,10):
        print(i)  # print 0 to 9

    print('-----')
    # while
    ind = 0
    nums = range(12)
    while ind < len(nums):
        print(nums[ind])
        ind += 2

    print('-----')

    # list methods (function call): direct list modification, donot return
    dream_bikes = ['Z900RS', 'RnineT', 'CB1300', 'CB1100', 'S1000RR']
    print(dream_bikes)
    dream_bikes.append('hayabusa')
    print(dream_bikes)
    dream_bikes.insert(1, 'R1')
    print(dream_bikes)
    dream_bikes.extend(['CB350', 'DRZ400'])
    print(dream_bikes)
    print(dream_bikes.index('CB1300'))
    #print(dream_bikes.index('Harley'))
    dream_bikes.remove('RnineT')
    print(dream_bikes)
    dream_bikes.reverse()
    print(dream_bikes)
    dream_bikes.pop(4)
    print(dream_bikes)
    dream_bikes.pop()
    print(dream_bikes)



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
