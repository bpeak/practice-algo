def solution(s):
    len_s = len(s)
    result = len_s
    for compress_char_count in range(1, (len_s // 2) + 1):
        curr_result = 0
        number_of_looping = len_s // compress_char_count if len_s % compress_char_count == 0 else len_s // compress_char_count + 1
        curr_compress_target_str = s[0:compress_char_count]
        curr_compress_target_str_count = 1
        compressed_str = ""
        for i in range(1, number_of_looping):
            curr_str = s[compress_char_count*i:compress_char_count*(i + 1)]
            if curr_str == curr_compress_target_str:
                curr_compress_target_str_count += 1
            else:
                compressed_str += ("" if curr_compress_target_str_count == 1 else str(curr_compress_target_str_count)) \
                     + curr_compress_target_str
                curr_compress_target_str_count = 1
                curr_compress_target_str = curr_str
        else:
            compressed_str += ("" if curr_compress_target_str_count == 1 else str(curr_compress_target_str_count)) \
                + curr_compress_target_str

        if(len(compressed_str) < result):
            result = len(compressed_str)
            
    return result

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17

"""
포커싱할 문자열 갯수 ( 1 ~ n )
    문자열을 포커싱할 문자열 갯수로 나눈 몫 만큼 루핑
        1. 포커스 문자를 가져옴 ( 기준 )
        2. 다음 문자를 가져옴
            같음 => 카운팅
            다름 => 카운팅 된 횟수만큼 빌드하고 1. 로
        루핑 이후 else 로 정리
"""