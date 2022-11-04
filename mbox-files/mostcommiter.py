fname = 'mbox-short.txt'
fh = open(fname)
counts = dict()
email = None
for lines in fh:
    if lines.startswith('From') and len(lines.split()) > 2:
        words = lines.split()
        email = words[1]
        counts[email] = counts.get(email, 0 ) + 1
mostcommiter = None
ncommit = 0
for k,v in counts.items():
    if v > ncommit:
        mostcommiter = k
        ncommit = v
print(mostcommiter, ncommit)
    
            
