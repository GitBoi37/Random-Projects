import csv, sys

strcounts = {}
seqstrcounts = []
e = -1
seq = ""
STRs = []
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
else:
    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            if e >= 0:
                ls = row[0].split(",")
                strcounts[ls[0]] = list(map(int, ls[1:len(ls)]))
            else:
                STRs = row[0].split(",")[1:len(row[0])]
                e = 0
    with open(sys.argv[2], "r") as f:
        seq = f.readline()
        seq = seq[0:len(seq)-1]

for s in STRs:
    j = len(s)
    lastOneIsSeq = False
    numSeq = 0
    maxSeq = 0
    i = 0
    while i < len(seq):
        while seq[i:j] == s:
            numSeq += 1
            if numSeq > maxSeq:
                maxSeq = numSeq
            i+=len(s)
            j+=len(s)
        numSeq = 0
        i += 1
        j += 1
    seqstrcounts.append(maxSeq)

for a in strcounts:
    #print(sorted(strcounts[a]))
    for e in seqstrcounts:
        if sorted(strcounts[a]) == sorted(seqstrcounts):
            print(a)
            quit()
print("No Match.")
