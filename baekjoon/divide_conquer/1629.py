def power_modulo(A, B, C):
    # 기저 사례: B가 0인 경우
    if B == 0:
        return 1 % C

    # 분할 정복을 사용하여 지수를 반으로 나누어 계산
    half = power_modulo(A, B // 2, C)
    # 결과값을 C로 나눈 나머지를 구하기 위해 중간 결과값에 대해 나머지 연산 수행
    result = half * half % C

    # B가 홀수인 경우, A를 한 번 더 곱해줌
    if B % 2 == 1:
        result = result * A % C

    return result

# 입력 받기
A, B, C = map(int, input().split())

# A를 B번 곱한 후, C로 나눈 나머지 출력
print(power_modulo(A, B, C))