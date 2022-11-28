def solution(A, B):
    answer = 0
    listA = list(A)

    for _ in range(len(A)):
        if ''.join(listA) == B:
            return answer

        listA.insert(0, listA.pop())
        answer = answer + 1

    return -1


print(solution("apple",	"elppa"))
