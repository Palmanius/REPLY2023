with open("input.txt") as f:
    x = [i.strip() for i in f.readlines()]

num = int(x[0])
x.pop(0)
increment = int(len(x)/num)
cases = []

while len(x) > 0:
    cases.append(x[:increment])
    x = x[increment:]

print(cases)


 