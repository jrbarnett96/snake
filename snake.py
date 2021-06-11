from random import randint

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body 
        self.direction = init_direction 
        self.dead = False
    

    def take_step(self, position):
        if not self.dead:
            self.body.insert(len(self.body), position)
            return self.body.pop(0)


    def set_direction(self, direction):
        self.direction = direction 


    def head(self):
        return self.body[-1]

    def extend_head(self, head_pos):
        self.body.insert(len(self.body), head_pos)


class Apple:
    def __init__(self, position, pt_val=1):
        self.pt_val = pt_val
        self.position = position


class Game:
    def __init__(self, height, width):
        self.score = 0
        self.height = height
        self.width = width
        self.board = [[None for i in range(width)] for j in range(height)] 
        self.snake = Snake([(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4)], UP)
        self.apple = self.generate_apple()
        self.update_board() 

    def generate_apple(self):
        apple_coords = (randint(0, self.width-1), randint(0, self.height-1))
        if apple_coords not in self.snake.body:
            return Apple(apple_coords)
        else:
            return self.generate_apple()

    def update_board(self, prev_tail=None):
        if prev_tail is not None:
            self.board[self.height - prev_tail[1] - 1][prev_tail[0]] = None
        for coord in self.snake.body:
            if coord == self.snake.head():
                self.board[self.height - coord[1] - 1][coord[0]] = 'X'
            else:
                self.board[self.height - coord[1] - 1][coord[0]] = 'O'
        self.board[self.height - self.apple.position[1] - 1][self.apple.position[0]] = 'A'


    def take_turn(self, direction=None):
        death_status = False
        head = self.snake.head()
        if direction is None:
            direction = self.snake.direction
        new_head_coords = ((head[0] + direction[0]) % self.width, 
                            (head[1] + direction[1]) % self.height)
        if new_head_coords == self.apple.position:
            # Consume apple --> extend snake
            self.snake.extend_head(new_head_coords)
            self.apple = self.generate_apple() 
            self.update_board()
        else:
            # Move snake
            prev_tail = self.snake.take_step(new_head_coords)
            self.update_board(prev_tail)
        self.snake.direction = direction

        if self.snake.body.count(self.snake.head()) > 1:
            self.snake.dead = True
        return not self.snake.dead


    def render(self):
        self.update_board()
        horizontal_border = "+" + self.width*"-" + "+"
        print(horizontal_border)
        for row_idx in range(self.height):
            row = self.board[row_idx]
            row_str = "|"
            for col_idx in range(self.width):
                if row[col_idx] is None:
                    row_str += " "
                else:
                    row_str += row[col_idx]
            row_str += "|"
            print(row_str)
        print(horizontal_border)