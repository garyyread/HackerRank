# Enter your code here. Read input from STDIN. Print output to STDOUT

# Get inputs
x,y,z,n = (int(input()) for _ in range (4))

# Find all possible cuboid points in order, where the sum a vetricie is not equal to some N
result = [[x,y,z] for x in range(x+1) for y in range(y+1) for z in range(z+1) if (x + y + z != n)]

# Print resulting list[list[x,y,z]]
print result