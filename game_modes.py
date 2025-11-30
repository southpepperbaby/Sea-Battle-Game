
import random
from game_logic import GameBoard

class Game:
    def __init__(self):
        self.board1=GameBoard()
        self.board2=GameBoard()
        self.current_player=1
        self.game_over=False
        self.winner=None

    def switch_player(self):
        if self.current_player==1:
            self.current_player=2
        else:
            self.current_player=1

    def make_shot(self,x,y):
        if self.game_over:
            return "game_over"

        if self.current_player==1:
            target_board=self.board2
        else:
            target_board=self.board1

        result=target_board.shoot(x,y)

        if result=="win":
            self.game_over=True
            self.winner=self.current_player

        if result=="miss":
            self.switch_player()

        return result


class TwoPlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.phase="setup1"

    def setup_phase_complete(self,player):
        if player==1 and self.phase=="setup1":
            self.phase="setup2"
            return True
        elif player==2 and self.phase=="setup2":
            self.phase="play"
            return True
        return False

    def get_current_phase(self):
        return self.phase


class BotPlayer:
    def __init__(self,difficulty="easy"):
        self.difficulty=difficulty
        self.last_hit=None
        self.hunt_mode=False
        self.targets=[]

    def make_move_easy(self,enemy_board):
        possible_targets=[]
        for y in range(enemy_board.size):
            for x in range(enemy_board.size):
                cell=enemy_board.field[y][x]
                if cell in [0,1]:
                    possible_targets.append((x,y))

        if possible_targets:
            return random.choice(possible_targets)
        return None

    def make_move_medium(self,enemy_board):
        while self.targets:
            x,y=self.targets.pop(0)
            cell=enemy_board.field[y][x]
            if cell in [0,1]:
                return (x,y)

        return self.make_move_easy(enemy_board)

    def update_after_shot(self,x,y,result):
        if result=="hit":
            self.last_hit=(x,y)
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<10 and 0<=ny<10:
                    if (nx,ny) not in self.targets:
                        self.targets.append((nx,ny))

        elif result=="destroy":
            self.targets=[]
            self.last_hit=None

    def make_move(self,enemy_board):
        if self.difficulty=="easy":
            return self.make_move_easy(enemy_board)
        else:
            return self.make_move_medium(enemy_board)


class SinglePlayerGame(Game):
    def __init__(self,difficulty="easy"):
        super().__init__()
        self.bot=BotPlayer(difficulty)
        self.phase="setup"
        self.board2.place_ships_randomly()

    def player_setup_complete(self):
        self.phase="play"

    def bot_turn(self):
        if self.current_player!=2:
            return None

        move=self.bot.make_move(self.board1)
        if move:
            x,y=move
            result=self.make_shot(x,y)
            self.bot.update_after_shot(x,y,result)
            return {"x":x,"y":y,"result":result}
        return None