# main.py
from game_logic import GameBoard
from game_modes import TwoPlayerGame, SinglePlayerGame
from gui import BattleshipGUI

def main():
    app = BattleshipGUI()
    app.run()

if __name__ == "__main__":
    main()
