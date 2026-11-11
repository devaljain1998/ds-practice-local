"""
Design and implement a Snake Game
LLD / Machine Coding

You are required to design and implement a Snake game similar to the classic Nokia mobile phone game.

The game is played on a rectangular board consisting of rows × cols cells.

Initial conditions
- The snake starts at a given coordinate on the board.
- Initially, the snake has a length of 1.
- A food item appears at a given coordinate.
- The player controls the snake using four directions: UP, DOWN, LEFT, and RIGHT.
Movement rules
1. On every move, the snake's head moves one cell in the requested direction.
2. The rest of the snake follows the previous position of the segment ahead of it.
3. When the snake eats food, its length increases by 1 and the score increases by 1.
4. A new food item appears after the previous food item has been consumed.
5. Food must never spawn on a cell occupied by the snake.
Game-over conditions
- The snake collides with itself.
- The snake moves outside the board (unless boundary wrapping is enabled).
Expected implementation

Design a SnakeGame object that maintains the complete game state and exposes a method similar to:
game.next_move(Direction.RIGHT)



The method should update the game state, detect collisions, handle food consumption, and return the resulting game status.

Your task: Implement the solution using clean object-oriented design, appropriate data structures, and unit tests.
"""

"""
Rough:
    game.next_move(Direction.RIGHT) -> Position,
"""
from collections import deque
from enum import Enum
from dataclasses import dataclass

@dataclass
class Snake:
    positions: deque[int]
    position_set: set[int]

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

direction_to_delta = {
    Direction.UP: (0, 1),
    Direction.DOWN: (0, -1),
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0),
}

class GameOverException(Exception):
    pass


class SnakeGame:
    def __init__(self, m: int, n: int, food_positions: list = []):
        self.snake: Snake = Snake(positions=deque(), position_set=set())
        self.food_positions = food_positions
        self.food_ptr = 0
        self.rows = m
        self.cols = n

    def next_move(self, direction: Direction):
        # Fetch the latest position:
        x, y = self.snake.positions[-1]
        # Fetch the delta position:
        dx, dy = direction_to_delta[direction]
        # New positions:
        newx, newy = (x+dx)%self.rows, (y+dy)%self.cols

        # See if new coordinates are not in the previous coordinates
        # if yes then snake has bitten itself:
        if (newx, newy) in self.snake.position_set:
            raise GameOverException('Game is over')

        # See if this a food position:
        if (newx, newy) == self.food_positions[self.food_ptr]:
            self.food_ptr += 1
            if self.food_ptr == len(self.food_positions):
                print('Game won!!')
                raise GameOverException('Game won.')
        else:
            # pop the last position:
            last_position = self.snake.positions.popleft()
            self.snake.position_set.remove(last_position)

        # add the new position to snake's current's position:
        self.snake.positions.append((newx, newy))
        self.snake.position_set.add((newx, newy))
        

        

        
