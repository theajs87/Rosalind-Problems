# Problem 4 - Rabbits and Recurrence Relations
fibfile = open('rosalind_fib.txt', 'r')
string = fibfile.read()

n = int(string[:2])
k = int(string[3:])
f1 = 1
f2 = 1
answer = 0
for i in range(n-1):
    f1, f2 = f2, k*f1 + f2
print(f1)