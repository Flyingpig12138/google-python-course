#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  # i = 1
  # while nums and i < len(nums):  # return True if nums is not empty
  #   if nums[i] == nums[i-1]:
  #     nums.pop(i)  # modifiy original list, thus do not increase counter i
  #   else:
  #     i += 1  # increase counter i to move to next element
  # return nums

  # +++official solution+++
  result = []
  for num in nums:
    if result == [] or result[-1] != num:  # order of conditions matters here!
      result.append(num)
  return result




# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # method 1: rudimentary
  # merged_list = []
  # i1 = 0  # index for list 1
  # i2 = 0  # index for list 2
  # while i1 < len(list1) and i2 < len(list2):
  #   if list1[i1] > list2[i2]:
  #     merged_list.append(list2[i2])  # be aware of the diff between append() and extend() == +=
  #     i2 += 1
  #   elif list1[i1] < list2[i2]:
  #     merged_list.append(list1[i1])
  #     i1 += 1
  #   else:
  #     merged_list.append(list1[i1])
  #     merged_list.append(list2[i2])
  #     i1 += 1
  #     i2 += 1
  # if len(list1) > len(list2):
  #   merged_list += list1[i1:]
  # elif len(list1) < len(list2):
  #   merged_list += list2[i2:]
  
  # return merged_list

  # comment on the rudimentary method: 
  # list1.append(list2) treats list2 as a single element (nested list)
  # list1.extend(list2) adds the elements of list2 to the end of the list1
  # if list2 = ['aa','bb'], and we do: 
  # list1.extend(list2[0]), since list2[0] is a string, and extend treats argument as iterable,
  # it will add 'a' and 'a' sepaarately as two char. 
  # The same goes to += method, which behaves in the same way as extend()  

  # +++official solution+++
  result = []
  while len(list1) > 0 and len(list2) > 0:
    if list1[0] < list2[0]:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))
  # add the rest (one of them is empty)
  result.extend(list1)
  result.extend(list2)
  return result

  """
  # method 2: simple
  merged_list = []
  merged_list.extend(list1)
  merged_list.extend(list2)
  merged_list.sort()
  return merged_list
  """

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])
  test(remove_adjacent([1, 1, 1, 4, 5, 6, 6, 6, 6, 6, 6, 10]), [1, 4, 5, 6, 10])
  test(remove_adjacent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [1, 2, 3, 4])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
