# Google's python class 
This respository keeps track of my learning journey following the Google's python class [link](https://developers.google.com/edu/python)

## Useful links
- The python standard library [link](https://docs.python.org/3/library/)
- List of all string methods [link](https://docs.python.org/3/library/stdtypes.html#string-methods)
- type hint [link](https://docs.python.org/3/library/typing.html)
- the big book of small python projects: [link](https://inventwithpython.com/bigbookpython/)
- Python data science handbook: [link](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Notes (by chapter)
### Strings
- **Immutable**: strings are immutable, which means once a string is created, it cannot be modified (like a constant)
    - To modify an existing string, a new string has to be created

### Lists
- **Mutable**: Lists are mutable, which means after a list is created, its element can be modified. 
- **Assignment**: assignment with `=` does not make a copy of the original list. Instead, assignment makes two variables point to the same list in the memory
    - example: 
    ```python
    my_bikes = ['XSR155', 'CB400SF']
    dream_bikes = my_bikes
    dream_bikes.append('Z900RS')
    print(my_bikes)
    >>>['XSR155', 'CB400SF', 'Z900RS']
    ```
- **`list.extend()` vs `list.append()`**: 
    - `list0.extend(list1)`: list1 is treated as an iterable, i.e., extend() will loop over all elements of list1, and add each to the end of list0
    - `list0.append(list1)`: list1 is treated as a single element, i.e., append() will add the entire list1 as one single element to the end of list0.
    - using operators such as `+` and `+=` gives similar behaviors to `extend()` 
    - examples: 
    ```python
    list0 = ['honda','kawasaki','yamaha']
    list1 = ['suzuki']
    list0.append(list1)
    print(list0)
    >>> ['honda','kawasaki','yamaha',['suzuki']]
    list0.extend(list1)  # list0 is reset
    print(list0)
    >>> ['honda','kawasaki','yamaha','suzuki']
    ``` 
    - another example with empty list
    ```python
    list0 = ['155','400','650','1000']
    list1 = []
    list0.append(list1)
    print(list0)
    >>> ['155','400','650','1000',[]]
    list0.extend(list1)  # list0 is reset
    print(list0)
    >>> ['155','400','650','1000']
    ```
    - another example with string list
    ```python
    list0 = ['honda','yamaha']
    list1 = []
    list1.append(list0[0])
    print(list1)
    >>> ['honda']  # list0[0] is a string, which is treated as a single element
    list1.extend(list0[0])
    print(list1)
    >>> ['h','o','n','d','a']  # list0[0] as a string is iterable, thus each single char is looped through and added separately 
    ```
### Sorting
- `sorted(*iterable*, key=*key*, reverse=*reverse*)`: sort a list in ascending order (default). 
    - `sorted()` returns a new list (sorted) and the original list is not changed.
    - Input *iterable*: any *iterables* such as number (sorted numerically) or char (sorted alphabetically)
    - Input *key*: function that set the sorting rule (e.g., len -> sort by length)
    - Input *reverse*: True/False: sorting order
        
