INF = 1e9
cost = [
    [0, 4, INF, 6],
    [3, 0, 7, INF],
    [5, INF, 0, 4],
    [INF, INF, 2, 0],
]

for k in range(len(cost)):
    for i in range(len(cost)):
        for j in range(len(cost)):
            # D(ij) < D(ik) + D(kj) ?
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for row in cost:
    print(row)

"""
논리적으로 풀때는
k일때 k와 연결된 점은 볼 필요가 없음 ( ex) k => or => k )

근데
코드상에서는 조건처리 해줄 필요가 없다 ( 어차피 갱신 시킬 수 없기 때문에 )

ex)
ik      ikkk
ki      kkki
=> 당연히 갱신불가능하지

결론> 논리적으론 해당점을 찝어서 관련된 모든점을 갱신해주고 자기자신은 보지 않는등 생각할게 있지만 코드는 굉장히 단순함
"""