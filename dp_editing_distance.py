word1 = input()
word2 = input()
dp = []
for i in range(len(word2) + 1):
    new_row = [0] * (len(word1) + 1)
    dp.append(new_row)

for i in range(len(dp)):
    dp[i][0] = i
for j in range(len(dp[0])):
    dp[0][j] = j

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = min((dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word2[i - 1] != word1[j - 1])))

print(dp[-1][-1])

