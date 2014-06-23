d = {}
t = {}

source = 'wk6_test1_1.txt'
with open(source) as f:
  d = set((int(line.strip()) for line in f))
print d
t = set((i for i in range(-10000, 10001) for j in d if i != j and i - j in d))
print t
