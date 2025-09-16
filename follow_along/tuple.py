import sys

def main():
    # tuple basics
    tuple = (1,2,'yo')
    print(len(tuple))
    print(tuple[2])
    # tuple[2] = 'yeah'  # NO, tuple is immutable
    
    # immutable or mutable
    tuple1 = (1,2,['ya','yo','ye'])
    tuple1[2][0] = 'yu' # list is mutable right? 
    print(tuple1)  # >>> (1,2,['yu','yo','ye'])

    # size-1 tuple
    tuple2 = (1)  # can, but tuple2 will be a diff type
    tuple3 = (1,) # size-1 tuple
    print(tuple2)  # >>> 1
    print(type(tuple2))  # >>> <class 'int'>
    print(type(tuple3))  # >>> <class 'tuple'> 
    
    # assignment 
    (x,y,z) = (3.14, 9.81, 1e-3)  # identical size: corresponding assignment
    print(y)

# standard boilerplate
if __name__ == "__main__":
    main()