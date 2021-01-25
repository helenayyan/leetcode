from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = deque(food)
        self.next_food = []
        if self.food:
            self.next_food = self.food.popleft()
        self.curr_pos = [0, 0]
        self.body = deque()
        self.body.append([0, 0])
        self.foods = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        move_dict = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        next_pos = [self.curr_pos[0] + move_dict[direction][0], self.curr_pos[1] + move_dict[direction][1]]

        if next_pos == self.next_food:
            if self.food:
                self.next_food = self.food.popleft()
            else:
                self.next_food = []

            self.curr_pos = next_pos
            self.foods += 1
        else:
            self.body.popleft()
            if next_pos[0] < 0 or next_pos[0] >= self.height or next_pos[1] < 0 or next_pos[
                1] >= self.width or next_pos in self.body:
                return -1
            self.curr_pos = next_pos

        self.body.append(next_pos)

        print(self.body)
        return self.foods

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)