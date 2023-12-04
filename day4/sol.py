import re

def part1():
    with open("day4/input.txt", "r") as f:
        d = [tuple(l.strip()[10:].split(" | ")) for l in f.readlines()]
        s = 0
        for w, c in d:
            w = set([eval(e) for e in w.split(" ") if e!=""])
            c = set([eval(e) for e in c.split(" ") if e!=""])
            s += 2**(len(w.intersection(c))-1) if len(w.intersection(c)) >= 1 else 0
        print(s)

def part2():
    with open("day4/input.txt", "r") as f:
        d = [len(set(l[0].split(" ")).intersection(set(l[1].split(" ")))) for line in [line.strip() for line in f.readlines()] if (l := re.sub("\s+", " ", line.split(": ")[1]).split(" | "))]
        c = {}
        res = 0
        for i in range(len(d)):
            g = c.get(i,0)+1
            res += g
            for j in range(d[i]):
                c[i+j+1] = c.get(i+j+1,0) + g
        print(res)


if __name__ == "__main__":
    part1()
    part2()