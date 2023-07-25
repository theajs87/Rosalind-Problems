# Problem 7 - Mendel's First Law
iprbfile = open("rosalind_iprb.txt","r")
lines = iprbfile.read().split()

k = int(lines[0])
m = int(lines[1])
n = int(lines[2])
t = k+m+n

prob = k / t + m / t * (k + 0.75 * (m - 1) + 0.5 * n) / (t-1) + n / t * (k + 0.5 * m) / (t-1)
print(prob)
