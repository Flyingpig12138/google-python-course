import sys
import re  # regular expression

def main():
    # regular expression: introduction
    str = "word: pig can fly meh? 12138"
    match = re.search(r'word: \w\w\w', str)
    if match: 
        # print(match)  # match is a match object that looks like: <re.Match object; span=(0, 9), match='word: pig'>
        print(match.group())  # match.group(): return the exact sub-string that matches
        print(match.span())   # match.span():  return a tuple (start, end)
        print(match.start())  # match.start()/match.end(): start and end indices
    else:
        print('did not found')

    print('example 1 -----')

    # example 1: search for pattern 'iii' in string 'piiig'
    str = 'piiig12138'
    # match = re.search(r'iii', str)
    # match = re.search(r'ing', str)  # match == None
    # match = re.search(r'..g', str)  # match.end() will be 5 even tho index is only up to 4
    # match = re.search(r'...38', str)
    # match = re.search(r'\d\d\d\d', str)  # four consecutive digits
    match = re.search(r'\w\d',str)
    print(match.group(), match.span())  # match.end() does not contain match str

    print('example 2 -----')

    # example 2: repetition
    str = 'flyingpiiiiig12138'
    str2 = 'xy1 2 3xx'
    match = re.search(r'i+', str)  # it will find the first 'i' at index 3 and return
    match = re.search(r'pi+', str) # here it searches for repeating  char 'i', not 'pi'
    match = re.search(r'\d\s*\d\s*\d', str2)
    match = re.search(r'^f\w+','foo bar')
    print(match.group())

    print('example 3 -----')

    # example 3: email
    str = "xyz alice_b#@google.com purple monkey"
    # match = re.search(r'\s.+@.+\.com', str)
    match = re.search(r'[\w.#-]+@[\w.#-]+', str)  # here [a-c] means range, but [...-] means char (put last)
    print(match.group())

    print('group extraction -----')

    # group extraction
    str = "hello world, I am trying to mess alice_b#@hotmail.com-iasdmk monkey never cramp? "
    match = re.search(r'([\w#]+)@([\w#]+\.com)',str)
    print(match.group(1), match.group(2))
    
    print('findall -----')
    
    # findall re.findall(): find all match,. return a list
    str = "purple alice@google.com, blah monkey bob@abc.com blah flyingpig12138@qq.com dishwasher"
    match = re.findall(r'[^e]at', 'cat, rat, fat, eat')
    match = re.findall(r'\w+@\w+.com', str)
    # match = re.findall(r'(\w+)@(\w+.com)', str)  # return each match as a tuple
    for email in match:
        print(email)

    print('findall with files -----')

    # findall with files (find # of sentences a.k.a # of full stops in the text)
    f = open('foo.txt', encoding = 'utf-8')
    str = re.findall(r'\w+\.', f.read())
    sentence = len(str)
    print(f"There are in total {len(str)} sentences in the text file.")  # f-string
    print("There are in total %d sentences in the text file." % len(str))  # % format string

    print('findall and groups -----')

    


# standard boilerplate
if __name__ == "__main__":
    main()
