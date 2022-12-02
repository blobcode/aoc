f = open('input.txt', 'r')
lines = f.readlines()

# matchups
table = {
    0: {0: 3, 1: 6, 2: 0},
    1: {0: 0, 1: 3, 2: 6},
    2: {0: 6, 1: 0, 2: 3},
  }

# answer
a1 = 0
a2 = 0

for l in lines:
  a, b = l.split()
  # convert to int
  a = ord(a) - ord("A")
  b = ord(b) - ord("X")

  # lookup table and compute scores
  a1 += table[a][b] + b + 1
  # determine target score
  e = (a + b - 1) % 3
  a2 += table[a][e] + e + 1

print("q1", a1)
print("q2", a2)