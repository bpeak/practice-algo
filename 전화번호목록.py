def solution(phone_book):
	for i in range(len(phone_book) - 1):
		for j in range(i + 1, len(phone_book)):
			num1 = phone_book[i]
			num2 = phone_book[j]
			if num1 == num2[:len(num1)] or num2 == num1[:len(num2)]:
				return False
	return True

a = ["119", "97674223", "1195524421"]
b = ["123","456","789"]	
c = ["12","123","1235","567","88"]	

print(solution(a)) # False
print(solution(b)) # True
print(solution(c)) # False

"""
< 다이렉트패스 못한 이유 >
전화번호 갯수 짤라서 (slice) 해서 비교하자는게 기본 아이디어 였는데
입력이 숫자로 들어오는것을 고려하지 않아서 int has no len() 에러 떨어짐
	=> 이거 내가 테스트케이스에 숫자로한거지 문제에선 문자였네...zzzzzzz

* 데이터타입을 항상 생각하자! ( 문제든 솔루션 내에서든 )

"""

# 집함수
a = [1,2,3]
b = ["a", "b", "c"]

print(list(zip(a, b)))

# startswith
a = "abc"
b = "abcde"
c = "zz"

print(b.startswith(a))
print(b.startswith(c))