# Enter your code here. Read input from STDIN. Print output to STDOUT

raw_input()
a = set(map(int,raw_input().split()))

raw_input()
b = set(map(int,raw_input().split()))

union = set(a.union(b))
inter = set(a.intersection(b))
sym_diff = set(union.difference(inter))

result = list(map(int,sym_diff))
result.sort()

for i in range(0,result.__len__()):
    print result.__getitem__(i)