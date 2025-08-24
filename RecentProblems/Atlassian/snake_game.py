"""
Design Snake Game

Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.

"""

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.board = []
        for _ in range(height):
            self.board.append([0 for _ in range(width)])

        self.food = food 
        self.curr_food = self.food.popleft()
        self.len = 1 
        self.pos = [(0,0)]

    def is_border(self, r, c):
        return r <0 or c < 0 or r >= self.width or r >= self.height


    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        if direction == "R":
            # update head 
            # loop through 



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

def test_snake_game():

    s = SnakeGame(5,5, [[4,4],[2,2,]])

    assert s