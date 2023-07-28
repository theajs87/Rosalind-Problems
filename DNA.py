# Problem 1 - Counting DNA Nucleotides
dnafile = open('rosalind_dna.txt', 'r')
s = dnafile.read()

slist = list(s)
aA = 0
aC = 0
aG = 0
aT = 0

for i in range(len(s)):
    if slist[i] == 'A':
        aA += 1
    if slist[i] == 'C':
        aC += 1
    if slist[i] == 'G':
        aG += 1
    if slist[i] == 'T':
        aT += 1
print(aA, aC, aG, aT)
