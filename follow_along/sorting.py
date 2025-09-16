import sys

def main():
  # sorted: numbers
  list1 = [8, 2, 3, 7, 1, 6, 5, 4]
  print(sorted(list1))  # return a new list (sorted)
  print(list1)

  # sorted: char
  list2 = ['a','c','f','d','z','r','s']
  print(sorted(list2))  # return a new list (sorted)
  print(list2)

  ## input argument
  list = ['Honda', 'yamaha', 'Suzuki', 'kawasaki']
  print(sorted(list))  # case sensitive
  print(sorted(list, reverse=True))
  print(sorted(list, key=len, reverse=False))  # key= is a function (i.e., len()), thus, sort by string length
  print(sorted(list, key=lambda x: x[-1], reverse=False))  # lambda argument: expression creates an anonymous function
  # the above statement sort the input list in reverse order, based on the last char of each string (thus irrelevant to case)
  # when tie, maintain original order (relative): stable sort


# standard boilerplate
if __name__ == "__main__":
    main()