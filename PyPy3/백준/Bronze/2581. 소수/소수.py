M = int(input())
N = int(input())
prime_list = []

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

for i in range(M, N+1):
    if is_prime(i) == True:
        prime_list.append(i)

if prime_list:  # prime_list가 비어있지 않은 경우
    print(sum(prime_list))
    print(prime_list[0])
else:
    print(-1)