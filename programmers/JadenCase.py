def solution(sentence):
    return " ".join([word.capitalize() for word in sentence.split(" ")])

print(solution("3people unFollowed me"))