#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # read the html file
  with open(filename, "rt", encoding="utf-8") as f:
    content = f.read()  # content is a string
    f.close()  # close file
  
  # search and print year
  match_year = re.search(r'Popularity in (\d+)', content)  # find match
  # print(match_year.group()[-4:])  # extract only the year (4 digits)
    
  # find all names and print
  match_names = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',content)
  # print(match_names)  # return a list of string tuples: (rank, name_male, name_female)

  # put all names into dict
  my_dict = {}  
  for tup in match_names:  # tup = ('rank','name_male','name_female')
    rank = int(tup[0])  # convert to int
    names = tup[1:]  # names: ('name_male','name_female')
    for name in names:
      if name in my_dict:  # found duplicate key
        my_dict[name] = min(rank, my_dict[name])  # accept better rank
      else: 
        my_dict[name] = rank  # add key-value pair
  
  # convert dict to list
  my_list = []
  for item in my_dict.items():
    my_list.append(f"{item[0]} {item[1]}")
  
  # sort list based on names
  my_sorted_list = sorted(my_list)

  # insert year in the beningin :)
  my_sorted_list.insert(0, match_year.group()[-4:])
  # print(my_sorted_list)

  # convert to summary text
  summary_text = '\n'.join(my_sorted_list) + '\n'

  # return
  return summary_text


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  print(sys.argv)
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # debug for baby*.html: 
  # print(args[])
  
  # go through each filenames
  for filename in args:
    # call extract_names() function
    summary_text = extract_names(filename)  
    # print or write file
    if summary:
      with open(f'{filename}.summary', 'w', encoding='utf-8') as f:
        f.write(summary_text)
    else: 
      print(summary_text)
  
  """ Part B:
  running babynames.py with all .html files as input: 
  simply running "./babynames.py --summaryfile baby*.html" in the terminal is not gonna work. 
  instead: do the following in terminal:
    for f in "baby*.html"; do python3 babynames.py --summaryfile "$f"; done
  this will automatically execute babynames.py multiple times, each with a distinctive .html file.
  """

if __name__ == '__main__':
  main()
