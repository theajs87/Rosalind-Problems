# FIB - Rabbits and Recurrence Relations
fibfile = open('rosalind_fib.txt', 'r')
string = fibfile.read().split()

n, k = int(string[0]), int(string[1])
f1, f2 = 1, 1

for i in range(n-1):
    f1, f2 = f2, k*f1 + f2
print(f1)
