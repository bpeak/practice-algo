#me
def solution(prices):
    answer = []
    for i in range(len(prices)):
        live = 0
        for j in range(i + 1, len(prices)):
            live += 1
            if prices[i] > prices[j]:
                break;
        answer.append(live)
    return answer
print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
"""
answer의 배열의 갯수는 prices배열의 갯수로 정해져있음
    => 미리 만들어 놓을 수 있음
        => 미리 해당하는 배열 만들어놓고 live 변수 없이 해당 배열에 바로 작업 가능 ( 엄밀히말하면 더 좋은 공간복잡도겠지 )
"""
# best
def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer