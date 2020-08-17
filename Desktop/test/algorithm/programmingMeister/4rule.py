def solution(arr: list) -> int:
    n = len(arr)
    mx = [[None for i in range(n)]for j in range(n)]
    mn = [[None for i in range(n)]for j in range(n)]

    def mndp(a, b):
        if a == b:  # 단 건의 숫자이면...
            mx[a][b] = int(arr[a])
            mn[a][b] = int(arr[a])
        if mn[a][b] != None:
            return mn[a][b]  # dp
        temp = []
        for i in range(a+1, b, 2):
            op = arr[i]
            if op == '+':  # 더하기일 때는 양 쪽 결과의 최소값을 더해주면 최소가 된다.
                temp.append(mndp(a, i-1)+mndp(i+1, b))
            elif op == '-':  # 오른쪽은 최소 빼주는오른쪽은 최대일 때 최소가 된다.
                temp.append(mndp(a, i-1)-mxdp(i+1, b))
        mn[a][b] = min(temp)
        return mn[a][b]

    def mxdp(a, b):
        if a == b:  # 단 건의 숫자이면...
            mx[a][b] = int(arr[a])
            mn[a][b] = int(arr[a])
        if mx[a][b] != None:
            return mx[a][b]  # dp
        temp = []
        for i in range(a+1, b, 2):
            op = arr[i]
            if op == '+':  # 더하기일 때는 양 쪽 결과의 최대값을 더해주면 최대가 된다.
                temp.append(mxdp(a, i-1)+mxdp(i+1, b))
            elif op == '-':  # 오른쪽은 최대 빼주는오른쪽은 최소일 때 최대가 된다.
                temp.append(mxdp(a, i-1)-mndp(i+1, b))
        mx[a][b] = max(temp)
        return mx[a][b]

    return mxdp(0, n-1)


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(	["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
