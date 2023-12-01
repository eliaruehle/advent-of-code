import os
import re

D = {"one" : "1", "two": "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def part1():
    with open(os.path.abspath("day1/input.txt"), "r") as f:
        d = [(lambda x: "".join(c for c in x if c.isdigit()))(l) for l in f.readlines()]
        return sum([eval((s[0]+s[-1])) for s in d])

def part2():
    p = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    s = 0
    with open(os.path.abspath("day1/input.txt"), "r") as f:
        for l in f.readlines():
           matches = re.findall(p, l)
           l, r = matches[0], matches[len(matches)-1]
           num = "" + getdigit(l) + getdigit(r)
           s += int(num)
        return s 

def getdigit(c:str):
    if c.isdigit():
        return c
    else:
        return D[c]

                
            





if __name__ == "__main__":
    print(part1())
    print(part2())