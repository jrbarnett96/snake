from snake import UP, DOWN, LEFT, RIGHT, Game, Snake, Apple

if __name__ == "__main__":
    direction_dict = {'W':UP, 'A':LEFT, 'S':DOWN, 'D':RIGHT, '':None}
    game = Game(20, 20)
    while game.take_turn(direction_dict[input()]):
        game.render()
    
        
