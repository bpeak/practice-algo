def solution(user_count, words):
    used_words = set()
    prev_word = None
    for i in range(0, len(words)):
        curr_word = words[i]
        curr_turn = (i // user_count) + 1
        curr_user_number = (i % user_count) + 1
        if curr_word in used_words:
            return [curr_user_number, curr_turn]
        used_words.add(curr_word)
        if not prev_word:
            prev_word = curr_word
            continue
        prev_word_last_char = prev_word[-1]
        curr_word_first_char = curr_word[0]
        if prev_word_last_char != curr_word_first_char:
            return [curr_user_number, curr_turn]
        prev_word = curr_word
    return [0, 0]

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])) # [3,3]
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])) # [0,0]
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])) #[1,3]

"""
이전단어를 저장 or 캐싱 할 필요 없이
i-1로 사용하는게 더 좋을듯
일단 코드상으로도 깔끔해지지만 그 이상으로
첫번째인지 체크하는 if문이 사라지니까
매번 if문을 안타도 되잖아

if not prev_word:
    prev_word = curr_word
    continue
처음에만 실행될 처음인지 아닌지 체크할 이 if 문이
매번 실행된다는건 말이 안되지
"""

def solution2(user_count, words):
    used_words = set()
    used_words.add(words[0])
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        curr_word = words[i]
        curr_turn = (i // user_count) + 1
        curr_user_number = (i % user_count) + 1
        if curr_word in used_words:
            return [curr_user_number, curr_turn]
        used_words.add(curr_word)
        prev_word_last_char = prev_word[-1]
        curr_word_first_char = curr_word[0]
        if prev_word_last_char != curr_word_first_char:
            return [curr_user_number, curr_turn]
    return [0, 0]

# print(solution2(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])) # [3,3]
# print(solution2(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])) # [0,0]
# print(solution2(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])) #[1,3]

"""
결국 조건은
1) 끝말잇기조건
2) 사용됐는지
두개임

근데 나는 set 을 사용해서 코드가 길어졌지만 
( 추가로 (i%user_count)+1 와 비슷한 코드들을 curr_turn, prev_word_last_cha 라는 변수에 대입해서 사용함으로써
  코드에 의미를 부여해서 진행하려다보니.. )
사실 list 슬라이스 방식 words[:i] 를 이용하면
이전에서 사용 됐는지 체크가능함
이쁘긴 이쁘지 깔끔하고

!!!but!!! 리스트에서 in 연산으로 체크하는것이기 때문에
O(n) 이라 성능적으로는 좋지 않다고 생각함 ( 추후 테스트해보자 )
set 을 사용하면 map처럼 O(1)로 가능하거든

https://stackoverflow.com/questions/2831212/python-sets-vs-lists
참고해보면
list 가 set 보다 반복은 미약하게나마 빠르지만
v in data 연산은 훨신 빠름 ( 맞네 )

"""

def solution_other(user_count, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:  
            return [(i%user_count)+1, (i//user_count)+1]
    else:
        return [0,0]

# print(solution_other(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])) # [3,3]
# print(solution_other(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])) # [0,0]
# print(solution_other(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])) #[1,3]