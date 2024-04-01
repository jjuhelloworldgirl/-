N = int(input())
F = list(input().split())
H = input()

count = 0
for _ in F:
    if _ == H:
        count += 1

print(count)