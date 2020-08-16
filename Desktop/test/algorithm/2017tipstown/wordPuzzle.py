# 재귀로 풀어봤는데 시간 초과가 남.
# dp로 푸는 방법.
def solution(strs, t):
    answer = 0
    dp = {}
    for i in range(len(t)):
        dp[i] = float('inf')
    for i in range(len(t)-1, -1, -1):
        for k in range(1, 6):
            if t[i:i+k] in strs:
                # 맨 오른쪽 범위 초과 방지를 위해 0을 default로 설정해준다.
                dp[i] = min(dp[i], dp.get(i+k, 0)+1)

    # 시간 복잡도는 6 * n*n. 재귀보다는 무조건 빠르곘다.
    return dp[0]
