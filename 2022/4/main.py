f = open("input.txt", "r")
lines = f.read().splitlines()


def part_1():
    s = 0

    for l in lines:
        # split into 2 parts
        p1, p2 = l.split(",")
        p1 = p1.split("-")
        p2 = p2.split("-")
        p1 = range(int(p1[0]), int(p1[1]) + 1)
        p2 = range(int(p2[0]), int(p2[1]) + 1)
        if set(p1).issubset(p2) or set(p2).issubset(p1):
            s += 1
    return s


def part_2():
    s = 0

    for l in lines:
        # split into 2 parts
        p1, p2 = l.split(",")
        p1 = p1.split("-")
        p2 = p2.split("-")
        p1 = range(int(p1[0]), int(p1[1]) + 1)
        p2 = range(int(p2[0]), int(p2[1]) + 1)
        if len(set(p1).intersection(set(p2))) > 0:
            s += 1
    return s


print(part_1())
print(part_2())
