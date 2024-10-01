#6_A
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n, n[:])
print(n[0], n[-10])
print(n[9], n[-1])
print(n[3:])
print(n[:5])
print(n[-5:-1])
print(n[4:8])
#B
print(n[-1] + n[-2])
print(n[9] - n[1])
print(n[2] * n[5])
print(n[8] / n[2])
print(len(n), n[:len(n)], sep = '\n')
print(min(n), max(n), type(n), sep = '\t')