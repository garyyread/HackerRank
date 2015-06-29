# Enter your code here. Read input from STDIN. Print output to STDOUT

# Throw...
_ = input()

# Map string input to integer SET, no repeated values, and sort
data = sorted(set(map(int, raw_input().split())))

# Print 2nd to last element of the sorted set
print data[-2]