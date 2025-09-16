import sys


def main():
    # list comprehension: [expr for var in list]
    nums = [1,2,3,4]
    squares = [n*n for n in nums]
    print(squares)  # [1,4,9,16]

    # adding !!! to string
    strs = ['hello', 'and', 'goodbye']
    shoutout = [s.upper()+'!!!' for s in strs]  # ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
    print(shoutout)

    # adding if condition to the right
    nums = [1,2,3,4,5,6,7,8,9,10]
    tri333ple = [n*n*n for n in nums if n < 5]
    print(tri333ple)  # [1, 8, 27, 64]

    ## adding if condition to the right (example 2)
    brand_names = ['honda','yamaha','suzuki','kawasaki','ducati','bmw','triumph']
    u_brand = [n for n in brand_names if 'u' in n]
    print(u_brand)

# standard boilerplate
if __name__ == "__main__":
    main() 