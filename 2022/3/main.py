f = open('input.txt', 'r')
lines = f.read().splitlines()


def value(char):
  if char.islower():
    return ord(char) - ord('a') + 1

  return ord(char) - ord('A') + 27


def part_1():
  s = 0
  
  for l in lines:
    # split into 2 parts
    n = len(l)
    r1 = l[0:n // 2]
    r2 = l[n // 2:]
    # char where intersect
    x = (set(r1) & set(r2)).pop()
    s += value(x)
  return s


def part_2():
  s = 0
  n = len(lines)
  
  # groups
  for i in range(0, n, 3):
    # char where intersect
    x = (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    s += value(x)
  return s


print(part_1())
print(part_2())
