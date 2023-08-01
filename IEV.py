# IEV - Calculating Expected Offspring
ievfile = open("rosalind_iev.txt","r")
s = ievfile.read().split()

n1 = int(s[0])
n2 = int(s[1])
n3 = int(s[2])
n4 = int(s[3])
n5 = int(s[4])
n6 = int(s[5])

p1 = 2
p2 = 2
p3 = 2
p4 = 1.5
p5 = 1
p6 = 0

e = n1*p1 + n2*p2 + n3*p3 + n4*p4 + n5*p5 + n6*p6
print(e)
