# N과 K를 한 줄로 입력받기
N, K = map(int, input().split())

# K번째 약수를 저장할 변수
kth_divisor = 0

# N의 약수 개수를 저장할 변수
divisor_count = 0

# 1부터 N까지의 수에 대해 반복하면서 약수를 찾음
for i in range(1, N + 1):
    if N % i == 0:
        divisor_count += 1
        if divisor_count == K:
            kth_divisor = i
            break

# 결과 출력
print(kth_divisor)