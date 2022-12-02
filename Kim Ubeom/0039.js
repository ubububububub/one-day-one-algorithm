function solution(s) {
  let answer = 0;
  const str = s.split(" ");

  for (let i = 0; i < str.length; i++) {
    if (str[i + 1] === "Z" || str[i] === "Z") {
      continue;
    }

    answer = answer + Number(str[i]);
  }

  return answer;
}

console.log(solution("1 2 Z 3"));
