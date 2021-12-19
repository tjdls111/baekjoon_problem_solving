import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

N = int(input())

dp = [0] * (max(N + 1, 8))

dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(8, N + 1):
    if dp[i] == 0:
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 5], dp[i - 7]) + 1

print(dp[N])
