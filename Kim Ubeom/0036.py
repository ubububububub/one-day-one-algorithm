def solution(spell, dic):
    sortedSpell = ''.join(sorted(spell))
    sortedDic = []

    for i in dic:
        sortedDic.append(''.join(sorted(list(i))))

    for i in sortedDic:
        if i == sortedSpell:
            return 1

    return 2


print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
