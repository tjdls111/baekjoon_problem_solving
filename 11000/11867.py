# 2가 어느 한 쪽에 있는 경우, 그때 답이 된다!!
# 그럼 최대한 상대방에게 2를 어느 한 쪽에 안 넘겨줘야 함. 어쩔 수 없이 넘겨주면 지게 됨..!!
# 짝수 -> 짝짝이나 홀홀로 바꿀 수 있음
# 홀수 -> 홀, 짝으로 바꿀 수 있음
# 짝수를 먼저 가지는 사람이 이긴다. -> A가 가지고 시작했냐, 그게 아니냐

N, M = map(int, input().split())
if N % 2 == 0 or M % 2 == 0:
    print('A')
else:
    print('B')
