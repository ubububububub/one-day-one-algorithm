function solution(sides) {
  const answer = [];
  const max = Math.max(...sides);
  const min = Math.min(...sides);

  for (let i = max - min + 1; i <= max; i++) {
    answer.push(i);
  }

  for (let i = max + 1; i < max + min; i++) {
    answer.push(i);
  }

  return answer.length;
}

console.log(solution([3, 6]));
