# Get data
string, substring = (raw_input() for _ in range(2))

# Iterate though string using sample size of substring.length()
counter = int()
for i in range(0, string.__len__() - substring.__len__() +1):
	# Increment counter if substring and 'substring' match
    counter = (counter + 1) if (string[i : i + substring.__len__() : 1] == substring) else (counter)
    
print counter