n = int(input())

dp = [float('inf')] * (n + 1)
dp[1] = 0

if n > 2:
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n + 1):

        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1)
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = dp[i - 1] + 1
    print(dp[n])

else:
    if n == 1:
        print(0)
