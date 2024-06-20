

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here

import argparse
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import re

parser = argparse.ArgumentParser()
# parser.add_argument("-h")
parser.add_argument("dir")
args = parser.parse_args()


cwd = os.getcwd()
path = os.path.join(cwd, args.dir)
if not os.access(path, os.F_OK):
    os.mkdir(path)

lst_sites = set()
STACK = deque()

while True:
    usr = input()
    if usr == "exit":
        break

    if usr == "back" and len(STACK) >= 2:
        STACK.pop()
        usr = STACK.pop()
    elif usr == "back" and len(STACK) < 2:
        continue

    if usr in lst_sites:
        with open(os.path.join(path, usr), "r") as f:
            print(f.read())

    if "." not in usr:
        print("Invalid URL")
        continue

    try:
        link = f"http://{usr}"
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.get_text())
        for tag in soup.find_all(re.compile("")):
            if tag.name == "a":
                print(Fore.BLUE + tag.text)
            elif tag.text:
                print(tag.text)

        with open(os.path.join(path, usr[:usr.index('.')]), "w") as f:
            f.write(soup.get_text())
            lst_sites.add(usr[:usr.index('.')])
            STACK.append(usr)
    except requests.exceptions.RequestException as e:
        print("Invalid URL")
        print(e)
