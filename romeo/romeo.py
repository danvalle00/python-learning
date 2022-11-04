fh = open('romeo.txt')
lst = list()
aux = list()
for line in fh:
    lst.append(line.split())
for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] not in aux:
            aux.append(lst[i][k]) 
aux.sort()
print(aux)            
