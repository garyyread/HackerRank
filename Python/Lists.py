# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(raw_input())
L = []
for i in range(0,size):
    query = (raw_input().split())
    
    if query[0].__contains__('print'):
        print L

    if query[0].__contains__('sort'):
        L.sort()

    if query[0].__contains__('append'):
        L.append(int(query[1]))

    if query[0].__contains__('remove'):
        L.remove(int(query[1]))

    if query[0].__contains__('reverse'):
        L.reverse()

    if query[0].__contains__('index'):
        L.index(int(query[1]))
        
    if query[0].__contains__('insert'):
        L.insert(int(query[1]),int(query[2]))

    if query[0].__contains__('count'):
        L.count()

    if query[0].__contains__('pop'):
        try:
            L.pop()
        except:
            print "Empty List."