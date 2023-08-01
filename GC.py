# GC - Computing GC Content
# Makeshift FASTA parser - ugly but am working to optimise it
FASTAFile = open("rosalind_gc.txt","r")
lines = FASTAFile.read().splitlines()
FASTAdict = {}
counter = []
ac = 0

for thing in range(len(lines)):
    if '>' in lines[thing]:
        counter.append(thing + 1)
        
for thing in range(len(lines)):
    if '>' in lines[thing]:
        lines[thing] = lines[thing].replace('>','')
        if len(counter) > ac + 1:
            newlist = lines[counter[ac]:(counter[ac + 1] - 1)]
        else:
            newlist = lines[counter[ac]:]
        ac += 1
        new_key = lines[thing]
        new_def = ''.join(newlist)
        FASTAdict.update({new_key : new_def})
# end of FASTA parser

GCdict = {}
GCcounter = 0
for key in FASTAdict:
    for i in range(len(FASTAdict[key])):
        if FASTAdict[key][i] == 'G' or FASTAdict[key][i] == 'C':
            GCcounter += 1
    GCpercent = 100 * (GCcounter / len(FASTAdict[key]))
    GCdict.update({key : GCpercent})
    GCcounter = 0
    
answer = max(GCdict, key = GCdict.get)
print(answer)
print(GCdict[answer])
