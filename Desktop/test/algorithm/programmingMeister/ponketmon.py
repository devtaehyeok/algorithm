
# 절반 갯수가 최대이고 아니면 겹치지 않는 갯수
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
