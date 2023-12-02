from typing import List

# order: red, green, blue

def part1() -> int:
    with open("day2/input.txt", "r") as f:
        # retrieve two dimensional array:
        games = [g.split(" ")[1:] for g in f.readlines()]
        id_sum = 0
        for g in games:
            id = int(g[0][:-1])
            if check_game(g[1:]):
                id_sum += id
    return id_sum 

def part2() -> int:
    with open("day2/input.txt", "r") as f:
        games = [g.split(" ")[2:] for g in f.readlines()]
        pow_sum = 0
        for g in games:
            pow_sum += get_min(g)
    return pow_sum


def check_game(g:List[str]) -> bool:
    
    for _ in range(int(len(g)/2)):
        n, c = int(g.pop(0)), g.pop(0)
        match c.replace(",", "").replace("\n", "").replace(";", ""):
            case "red":
                if n > 12:
                    return False
            case "green":
                if n > 13:
                    return False
            case "blue":
                if n > 14:
                    return False
    return True

def get_min(g:List[str]) -> int:
    
    cm = [0,0,0]
    for _ in range(int(len(g)/2)):
        n, c = int(g.pop(0)), g.pop(0)
        match c.replace(",", "").replace("\n", "").replace(";", ""):
            case "red":
                cm[0] = max(cm[0], n)
            case "green":
                cm[1] = max(cm[1], n)
            case "blue":
                cm[2] = max(cm[2], n)
    return cm[0]*cm[1]*cm[2]
        






if __name__ == "__main__":
    print(part1())
    print(part2())