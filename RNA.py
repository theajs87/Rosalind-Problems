# Problem 2 - Transcribing DNA into RNA
rnafile = open('rosalind_rna.txt', 'r')
t = rnafile.read().rstrip()

length = list(t)
for i in range(len(t)):
    if length[i] == 'T':
        length[i] = 'U'
''.join(length)
