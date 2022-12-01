i = open("1.txt", "r").read()
i = i.split("\n\n")
out = []

for each in i:
  nums = each.split("\n")
  out.append(sum([int(x) for x in nums]))
out.sort()

a = out[-1]
b = sum(out[-3:])

print(a, b)