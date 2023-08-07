dp = [0] * (t - 1)
for i in range(t-1): 
    result += v1 + bonus 
    dp[i] = v1 + bonus
    bonus += d
result += v2
# print('result', result)
# print('dp', dp)
lastSpeed = v2 
for i in range(len(dp) - 1, -1, -1): 
    diff = abs(lastSpeed - dp[i]) - d 
    # print('diff', diff)
    if diff > 0: 
        result -= diff
        dp[i] -= diff
    lastSpeed = dp[i]
# print('result', result)
# print('dp', dp)
print(result)