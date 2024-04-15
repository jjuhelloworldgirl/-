N = int(input())

found = False

for i in range(max(1, N - 9 * len(str(N))), N):
    icount = 0
    for j in str(i):
        icount += int(j)
    if N-i == icount or N == i:
        print(i)
        found = True
        break

if not found:
    print(0)