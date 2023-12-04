import re

def part1():
    with open("day3/input.txt", "r") as f:
        g = ["." + l.strip() + "." for l in f.readlines()]
        d = [re.findall(r'\b\d+\b', l) for l in g]
        g.insert(0, len(g[0])*'.')
        g.append(len(g[0])*'.')
        s = 0
        for i in range(1, len(g)-1, 1):
            p=0
            for n in d[i-1]:
                p = g[i].find(n, p, len(g[i]))
                for j in range(len(n)):
                    if any([(bool(re.search(r'[^0-9.]', e))) for e in [g[i][(p+j)-1], g[i][(p+j)+1], g[i-1][(p+j)], g[i+1][p+j], g[i-1][(p+j)-1], g[i-1][(p+j)+1], g[i+1][(p+j)-1], g[i+1][(p+j)+1]]]):
                        s += int(n)
                        break
        print(s)
                    
def part2():
    with open("day3/input.txt", "r") as f:
        g = ["." + l.strip() + "." for l in f.readlines()]
        g.insert(0, len(g[0])*'.')
        g.append(len(g[0])*'.')
        r = 0
        for i in range(1, len(g)-1, 1):
            for j in range(1, len(g[i])-1, 1):
                if g[i][j] == "*":
                    numbers = set()
                    n = [(i,j-1), (i,j+1), (i-1,j), (i+1,j), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]
                    for si, sj in n:
                        start = sj
                        if not g[si][sj].isnumeric():
                            continue
                        while True:
                            if g[si][start].isnumeric():
                                start -= 1
                            else:
                                start += 1
                                break
                        num = ""
                        while g[si][start].isnumeric():
                            num += g[si][start]
                            start += 1
                        numbers.add(num)
                    if len(numbers) == 2:
                        t = 1
                        for e in numbers:
                            t *= int(e)
                        r += t
        print(r)

if __name__ == "__main__":
    part1()
    part2()