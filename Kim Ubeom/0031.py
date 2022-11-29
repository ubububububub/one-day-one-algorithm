def solution(quiz):
    print(quiz[0].split())
    answer = []

    for i in quiz:
        middleAnswer = 0
        [left, operator, right, _, result] = i.split()

        if operator == '+':
            middleAnswer = int(left) + int(right)
        elif operator == '-':
            middleAnswer = int(left) - int(right)

        if middleAnswer == int(result):
            answer.append("O")
        else:
            answer.append("X")

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
