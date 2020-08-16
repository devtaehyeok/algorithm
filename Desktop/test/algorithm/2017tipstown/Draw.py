def solution(n: int, a: int, b: int) -> int:
    # 1과 2의 경우 0001 0010  -> 0000 0001 첫번째
    # 3과 8의 경우 0011 1000 -> 0010 0111 3번째
    return ((a-1) ^ (b-1)).bit_length()
