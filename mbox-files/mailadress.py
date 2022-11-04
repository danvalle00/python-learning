fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
data= list()
for k in fh:
    if k.startswith("From") and len(k.split())>2:
        temp=k.split()
        data.append(temp[1])
for k in data:
    print(k)
print("There were", len(data), "lines in the file with From as the first word")
