# Problem 6 - Counting Point Mutations
hammfile = open('rosalind_hamm.txt', 'r')
string = ''.join(hammfile.read().splitlines())

s = string[:len(string)//2]
t = string[len(string)//2:]

S = list(s)
T = list(t)
counter = 0

for i in range(len(string)//2):
    if S[i] != T[i]:
        counter +=1 

print(counter)
