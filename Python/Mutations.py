word = raw_input()
data = raw_input().strip().split()
index = int(data[0])
letter =  data[1]

word = word[:index] + letter + word[index + 1:]

print word