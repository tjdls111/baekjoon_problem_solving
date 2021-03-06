N = int(input())
dp = [0, 0, 1, 1] + [0] * N  # 0, 1번 인덱스는 편하게 쓰려고 추가. 2에서 1로 가는 최소 연산 수는 1, 3에서 1로 가는 최소 연산 수는 1개.

for i in range(4, N + 1):  # N을 구해야 하니까 그때까지 보기
    if i % 6 == 0:  # i가 2, 3으로 나누어 떨어지는 경우 -> 연산 1, 2, 3 중에 가장 횟수 적은 것을 dp에 저장
        dp[i] = min(1 + dp[i // 3], 1 + dp[i // 2], 1 + dp[i - 1])
    elif i % 2 == 0:  # i가 3으로는 나누어 떨어지지 않고, 2로 나누어 떨어지는 경우 -> 연산 2, 3 중에 가장 횟수 적은 것을 dp에 저장
        dp[i] = min(1 + dp[i // 2], 1 + dp[i - 1])
    elif i % 3 == 0:  # i가 2로는 나누어 떨어지지 않고, 3으로 나누어 떨어지는 경우 -> 연산 1, 3 중에 가장 횟수 적은 것을 dp에 저장
        dp[i] = min(1 + dp[i // 3], 1 + dp[i - 1])
    else:  # i가 2나 3으로 나누어 떨어지지 않는 경우 -> 연산 3
        dp[i] = 1 + dp[i - 1]
# print(dp)
print(dp[N])
