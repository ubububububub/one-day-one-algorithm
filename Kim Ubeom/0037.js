function solution(keyinput, board) {
  const horizontal = Math.floor(board[0] / 2);
  const vertical = Math.floor(board[1] / 2);
  let xPos = 0;
  let yPos = 0;

  for (const dir of keyinput) {
    if (
      (dir === "right" && xPos === horizontal) ||
      (dir === "left" && xPos === horizontal * -1)
    ) {
      continue;
    }

    if (
      (dir === "up" && yPos === vertical) ||
      (dir === "down" && yPos === vertical * -1)
    ) {
      continue;
    }

    if (dir === "left") {
      xPos = xPos - 1;
    } else if (dir === "right") {
      xPos = xPos + 1;
    } else if (dir === "up") {
      yPos = yPos + 1;
    } else if (dir === "down") {
      yPos = yPos - 1;
    }
  }

  return [xPos, yPos];
}

console.log(solution(["left", "left", "left", "right"], [3, 3]));
