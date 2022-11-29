def solution(n):
    answer = []
    end = n
    num = 2

    while n >= 2:
        if end == num:
            answer.append(num)
            break

        if n % num == 0:
            answer.append(num)
            n = n // num
            num = 2
            continue

        num = num + 1

    return sorted(list(set(answer)))


print(solution(33))
