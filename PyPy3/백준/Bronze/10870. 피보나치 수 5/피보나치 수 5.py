N = int(input())

F0 = 0
F1 = 1

if N == 0:
    print(F0)
elif N == 1:
    print(F1)
else:
    for _ in range(N-1):
        temp = F0 + F1
        F0 = F1
        F1 = temp

    print(temp)
