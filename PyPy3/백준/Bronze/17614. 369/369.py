# 박수 횟수를 세는 함수
def count_claps(number):
    count = 0
    for digit in str(number):
        if digit in ['3', '6', '9']:
            count += 1
    return count

clap = 0  # clap의 초기값 설정

# 사용자로부터 N 입력 받기
N = int(input().strip())
if N < 1 or N > 10**6:
    print("입력 범위를 초과했습니다. 1에서 10의 6승 사이의 값을 입력하세요.")
else:
    # 1부터 N까지의 수에 대해 반복
    for i in range(1, N + 1):
        clap += count_claps(i)

    # 결과 출력
    print(clap)
