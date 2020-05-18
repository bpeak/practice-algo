def solution(tops):
    result = [0] * len(tops)
    for i in range(len(tops)):
        for j in range(i - 1, 0 - 1, -1):
            if tops[j] > tops[i]:
                result[i] = j + 1
                break                      
    return result

"""
사고적으로는 쉬운 문제였음에도 불구하고
한번에 통과를 못했음 ( 실수 )

1) 요구조건 정확히 파악 ( 탑의 인덱스를 리턴해달라고 했음 => 나는 높이를 리턴함 )
2) 인덱스관련해서는 예민하게 ( 현재 탑의 번호는 1부터임 => 인덱스 + 1 이 탑 번호 )
3) 인덱스와 값을 동시에 사용할때 보통 enumerate를 사용하지
	근데 항상 좋은건 아님 ( idx, value 같이 꺼내는게 )
	특히 이중포문이면서 동시에 idx, value 다 사용하는경우 ( i, j, v1, v2 )
	그냥 인덱스 i, j 로만 돌리고
	값을 arr[i] arr[j] 로 접근하는게 더 명확할 수 있다. ( 실수를 줄일 수 있다. )
"""