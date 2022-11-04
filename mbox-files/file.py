fname = input("Enter file name: ")
fh = open(fname)
scount, vcount = 0, 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue    
    scount += 1
    vcount += float(line[line.find(':')+1:].rstrip())
print(f"Avarage spam confidence: {vcount/scount}")
print("Done")