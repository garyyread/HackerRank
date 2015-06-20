# Enter your code here. Read input from STDIN. Print output to STDOUT

# Number of items to add to dictionary
items = int(input())

# Add items to dictionary
dic = {}
for items in range(0,items):
    item = raw_input().split()
    dic[item[0]] = (float(item[1]),float(item[2]),float(item[3]))
    
# Calculate average from specific user and print
query = raw_input()
if query in dic:
    sum = 0.00
    query_res = dic[query]
    
    length = query_res.__len__()
    for i in range(0,length):
        sum += query_res[i]

    print "%.2f" % (sum / length)
else:
    print query + " does not exist."