"""
This code is written in Python 3
"""
import re
fh = open("irish.txt", "r")
infile = fh.read()
def use_regex(file_name):
    if type(file_name) != str:
        raise TypeError
    all_words = re.findall(r"\w+at\b",file_name)
    for x in all_words:
        words = list(filter(lambda x: len(x)>3, all_words))
    print (words)
use_regex(infile)
