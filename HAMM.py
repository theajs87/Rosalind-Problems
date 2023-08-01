# HAMM - Counting Point Mutations
hammfile = open('rosalind_hamm.txt', 'r')
string = hammfile.read().split()

s = string[0]
t = string[1]

S = list(s)
T = list(t)
counter = 0

for i in range(len(s)):
    if S[i] != T[i]:
        counter +=1 

print(counter)
