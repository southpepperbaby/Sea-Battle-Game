# main.py
from game_logic import GameBoard
from game_modes import TwoPlayerGame, SinglePlayerGame
from gui import BattleshipGUI

def main():
    app = BattleshipGUI()
    app.run()

if __name__ == "__main__":
    main()

def start_vs_friend(self):
    """Начать игру с другом"""
    from game_modes import TwoPlayerGame

    self.game = TwoPlayerGame()

    # Сначала первый игрок расставляет
    self.setup_placement_screen(
        "Игрок 1",
        self.game.board1,
        self.player1_ready
    )

def player1_ready(self):
    """Игрок 1 закончил расстановку"""
    self.game.setup_phase_complete(1)

    # Показываем сообщение
    self.show_message(
        "Передайте компьютер Игроку 2",
        lambda: self.setup_placement_screen(
            "Игрок 2",
            self.game.board2,
            self.player2_ready
        )
    )

def player2_ready(self):
    """Игрок 2 закончил расстановку"""
    self.game.setup_phase_complete(2)
    self.setup_game_screen(self.game, "Игрок 1", "Игрок 2")

def start_vs_bot(self):
    """Начать игру с ботом"""
    from game_modes import SinglePlayerGame

    self.game = SinglePlayerGame(difficulty="medium")

    self.setup_placement_screen(
        "Вы",
        self.game.board1,
        self.start_bot_game
    )

def start_bot_game(self):
    """Начать игру после расстановки"""
    self.game.player_setup_complete()
    self.setup_game_screen_vs_bot()

def show_message(self, text, on_continue):
    """Показать сообщение с кнопкой продолжить"""
    for widget in self.window.winfo_children():
        widget.destroy()

    label = tk.Label(self.window, text=text, font=("Arial", 16))
    label.pack(pady=50)

    btn = tk.Button(
        self.window,
        text="Продолжить",
        command=on_continue
    )
    btn.pack()
