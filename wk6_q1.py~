d = {}
t = {}

source = 'wk6_test1_1.txt'

f = open(source)
for line in f:
    num = line.split()
    num = num[0]
    d[str(num)] =1

for i in range(0,20001):
    num = i - 10000
    numS = str(num)
    t[numS] = 0

for key in d:
    for i in range(0,20001):
        num = i - 10000
        y = num - int(key)
        if y != int(key):
            if str(y) in d.keys():
                t[num] = 1
                print int(key),y,num
            

print(d.keys())
print(sum(t.values()))


