# REVC - Complementing a Strand of DNA
revcfile = open('rosalind_revc.txt', 'r')
s = revcfile.read().rstrip()

scl = list(s)
for i in range(len(s)):
    if scl[i] == 'T':
        scl[i] = 'A'
    elif scl[i] == 'A':
        scl[i] = 'T'
    elif scl[i] == 'G':
        scl[i] = 'C'
    elif scl[i] == 'C':
        scl[i] = 'G'
''.join(scl)[::-1]
