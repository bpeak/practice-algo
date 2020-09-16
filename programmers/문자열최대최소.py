def solution(numbers_string):
    numbers = [int(v) for v in numbers_string.split(" ")]
    max_number = max(numbers)
    min_number = min(numbers)
    return f'{str(min_number)} {str(max_number)}'


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))