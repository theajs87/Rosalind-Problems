# Problem 9 - Finding a Motif in DNA
subsfile = open("rosalind_subs.txt","r")
string = subsfile.read().split()
s = string[0]
t = string[1]
counter = 0
answer = []

for i in range(len(s)):
    if s.startswith(t):
        answer.append(i+1)
    counter += 1
    s = s[1:]

print(" ".join(str(x) for x in answer))
