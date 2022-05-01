"""
Pull question from Project Euler and builds a file
785 total questions
"""
from bs4 import BeautifulSoup as bs
import requests
from os.path import exists
from os import system
import os
import time

start_time = time.time()

clear = lambda: system('cls')
clear()

#Config
Problem = 29

#Code
Link = 'https://projecteuler.net/minimal={}'.format(Problem)

r = requests.get(Link)
soup = bs(r.text, "html.parser")
containSup = ""
#print(soup)
if soup.find_all('sup'):
    containSup = "\nWarning, this question contains Sup"
    print(containSup)
Question = soup.get_text().strip()
#print(Question)
template = """
\"""
https://projecteuler.net/problem={}
{}
{}
\"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem{}(num):
    return 0

num = 0
print(problem{}(num))

print("--- {} seconds ---".format(time.time() - start_time))
print("\\n\\n")

#Answer is

""".format(Problem,Question,containSup,Problem,Problem, "{}")
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "Problem {}.py".format(Problem)

filename = os.path.join(dir_path,filename)
if exists(filename):
    print("{} already exists!".format(filename))
else:
    file = open(filename,"w",encoding="utf-8")
    file.write(template)
    file.close()
    print("{} is created!".format(filename))

print("\n\n--- {} seconds ---".format(time.time() - start_time))
print("\n\n")