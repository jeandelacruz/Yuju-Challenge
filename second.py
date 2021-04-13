def solution(A, B, K):
    if A == B and B == 0:
        return 1
    if A > 0:
        return B // K - (A - 1) // K
    if A == 0:
        return B // K + 1
    return 0

print(solution(6, 11, 2))
