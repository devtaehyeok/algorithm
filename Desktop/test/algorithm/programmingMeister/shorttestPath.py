# https://programmers.co.kr/learn/courses/30/lessons/1844 프로그래머스 게임맵 최단거리.
# 이런 문제는 항상 queue로 푸는 습관 (maximum recursion depth 빡쳐... ㅡㅡ...)
from collections import deque


def solution(maps):
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visited = {}
    q = deque()
    q.append((0, 0, 1))
    visited[(0, 0)] = 1
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (len(maps)-1, len(maps[0])-1):
            return cnt  # bfs를 하기 때문에 최단거리가 보장됨.
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if maps[ny][nx] == 1 and (ny, nx) not in visited:
                    visited[(ny, nx)] = 1
                    q.append((ny, nx, cnt+1))
    return -1


# test cases
print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
