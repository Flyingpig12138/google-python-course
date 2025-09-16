#! /usr/bin/env python3
import sys


def main():
    f = open('foo.txt', 'rt')  # read and write
    for line in f: 
        print(line)
    f.close()






# standard boilerplate
if __name__ == "__main__":
    main()
