# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
tup = tuple(map(int,raw_input().split()))

print tup.__hash__()