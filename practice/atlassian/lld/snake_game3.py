from dataclasses import dataclass
from enum import Enum
from collections import deque
from typing import List


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


str_to_direction_mp = {
    'U': Direction.UP,
    'D': Direction.DOWN,
    'L': Direction.LEFT,
    'R': Direction.RIGHT
}


@dataclass(frozen=True)
class Position:
    x: int
    y: int


class Snake:
    def __init__(self, starting_position: Position):
        # Front of the deque (index 0) is the head, back is the tail.
        self.positions: deque[Position] = deque([starting_position])
        self.position_set: set[Position] = {starting_position}

    @property
    def head(self) -> Position:
        return self.positions[0]

    def add_head(self, pos: Position) -> None:
        self.positions.appendleft(pos)
        self.position_set.add(pos)

    def remove_tail(self) -> None:
        tail = self.positions.pop()
        self.position_set.remove(tail)


@dataclass
class Board:
    height: int
    width: int

    def in_bound(self, pos: Position) -> bool:
        return (
            0 <= pos.x < self.height and
            0 <= pos.y < self.width
        )


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake: Snake = Snake(Position(0, 0))
        self.board: Board = Board(height, width)
        self.food_idx = 0
        self.food_positions: list[Position] = [Position(r, c) for r, c in food]
        self.score = 0

    def move(self, direction: str) -> int:
        dx, dy = str_to_direction_mp[direction].value
        head = self.snake.head
        new_head = Position(head.x + dx, head.y + dy)

        # Wall collision
        if not self.board.in_bound(new_head):
            return -1

        ate_food = (
            self.food_idx < len(self.food_positions)
            and new_head == self.food_positions[self.food_idx]
        )

        if ate_food:
            # Grow: keep the tail
            self.food_idx += 1
            self.score += 1
        else:
            # Tail moves out of the way before the self-collision check
            self.snake.remove_tail()

        # Self collision
        if new_head in self.snake.position_set:
            return -1

        self.snake.add_head(new_head)
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)