def solution(my_string):
    answer = 0
    expression = my_string.split()
    print(expression)

    answer = answer + int(expression[0])

    for i in range(1, len(expression) - 1):
        if expression[i] == '+':
            answer = answer + int(expression[i + 1])
        elif expression[i] == '-':
            answer = answer - int(expression[i + 1])

    return answer


print(solution("19640 - 6060 - 1000"))
