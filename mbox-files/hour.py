name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for l in handle:
    if l.startswith("From") and len(l.split()) > 2:
        wds = l.split()
        tmp = wds[5].split(':')
        hour = tmp[0]
        counts[hour] = counts.get(hour, 0) + 1
for k,v in sorted([(k,v) for k,v in counts.items()]):
    print(k, v)                   