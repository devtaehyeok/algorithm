def solution(s):
    q = []
    for c in s:
        if q and c == q[-1]:
            q.pop()
            continue
        q.append(c)
    return 1 if not q else 0
