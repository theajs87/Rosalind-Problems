# DNA - Counting DNA Nucleotides
dnafile = open('rosalind_dna.txt', 'r')
s = dnafile.read().rstrip()

aA, aC, aG, aT = 0, 0, 0, 0

for i in s:
    if i == 'A':
        aA += 1
    elif i == 'C':
        aC += 1
    elif i == 'G':
        aG += 1
    elif i == 'T':
        aT += 1
        
print(aA, aC, aG, aT)
