def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    count = 1

    for _ in range(len(emergency)):
        maxValue = max(emergency)
        maxIndex = emergency.index(maxValue)

        answer[maxIndex] = count
        count = count + 1

        emergency[maxIndex] = 0

    return answer


print(solution([30, 10, 23, 6, 100]))
