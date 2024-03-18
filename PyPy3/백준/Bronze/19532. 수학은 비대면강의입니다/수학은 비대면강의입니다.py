def solve_equations(a, b, c, d, e, f):
    # 연립 방정식 풀기(가우스 소거법)
    determinant = a * e - b * d
    if determinant != 0:
        x = (c * e - b * f) // determinant
        y = (a * f - c * d) // determinant

        # 결과가 주어진 범위 내에 있는지 확인
        if -999 <= x <= 999 and -999 <= y <= 999:
            # 해 출력
            print(x, y)
        else:
            print("주어진 범위에서 해가 존재하지 않습니다.")
    else:
        print("역행렬이 존재하지 않아 해를 찾을 수 없습니다.")

if __name__ == "__main__":
    # 변수 입력 받기
    a, b, c, d, e, f = map(int, input().split())
    solve_equations(a, b, c, d, e, f)


