def solution(my_string):
    answer = 0
    temp = '0'

    for i in range(len(my_string)):
        if not my_string[i].isnumeric():
            answer = answer + int(temp)
            temp = '0'
            continue
        temp = temp + my_string[i]

    return answer + int(temp)


print(solution("a1b23"))
