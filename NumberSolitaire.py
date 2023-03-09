import sys

def solution(A):
    N = len(A)
    dp = [-sys.maxsize] * N
    dp[0] = A[0]
    for i in range(1, N):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i-j] + A[i])
    return dp[N-1]
