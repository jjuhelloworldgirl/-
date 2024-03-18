N = int(input())
number = list(map(int, input().split()))
count = 0

for num in number:
  is_prime = True
  if num < 2:
    is_prime = False
  else:
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      count += 1

print(count)