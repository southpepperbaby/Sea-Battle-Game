import tkinter as tk
class BattleshipGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Морской бой")
        self.cell_size = 30
        self.field_size = 10
        self.colors = {
            0: "lightblue",
            1: "gray",
            2: "white",
            3: "orange",
            4: "red"
        }
        self.setup_main_menu()
    def setup_main_menu(self):
        """Главное меню"""
        for widget in self.window.winfo_children():
            widget.destroy()
        title = tk.Label(self.window, text="МОРСКОЙ БОЙ", font=("Arial", 24))
        title.pack(pady=20)
        btn_vs_friend = tk.Button(
            self.window,
            text="Играть с другом",
            font=("Arial", 14),
            command=self.start_vs_friend
        )
        btn_vs_friend.pack(pady=10)
        btn_vs_bot = tk.Button(
            self.window,
            text="Играть с компьютером",
            font=("Arial", 14),
            command=self.start_vs_bot
        )
        btn_vs_bot.pack(pady=10)
    def start_vs_friend(self):
        """Начать игру с другом"""
        print("Игра с другом")
    def start_vs_bot(self):
        """Начать игру с ботом"""
        print("Игра с ботом")
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    app = BattleshipGUI()
    app.run()


def create_field_canvas(self, parent, title, clickable=False, click_callback=None):
    """Создать канвас с игровым полем"""
    frame = tk.Frame(parent)
    label = tk.Label(frame, text=title, font=("Arial", 12))
    label.pack()
    canvas = tk.Canvas(
        frame,
        width=self.cell_size * self.field_size,
        height=self.cell_size * self.field_size
    )
    canvas.pack()

    for i in range(self.field_size + 1):
        x = i * self.cell_size
        canvas.create_line(x, 0, x, self.field_size * self.cell_size)
        canvas.create_line(0, x, self.field_size * self.cell_size, x)
    if clickable and click_callback:
        canvas.bind("<Button-1>", lambda e: self.on_field_click(e, click_callback))
    return frame, canvas


def on_field_click(self, event, callback):
    """Обработка клика по полю"""
    x = event.x // self.cell_size
    y = event.y // self.cell_size
    if 0 <= x < self.field_size and 0 <= y < self.field_size:
        callback(x, y)


def draw_field(self, canvas, field_data):
    """Отрисовать поле по данным"""
    for y in range(self.field_size):
        for x in range(self.field_size):
            cell = field_data[y][x]
            color = self.colors.get(cell, "lightblue")
            x1 = x * self.cell_size
            y1 = y * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
def setup_placement_screen(self, player_name, board, on_complete):
    """Экран расстановки кораблей"""
    for widget in self.window.winfo_children():
        widget.destroy()
    self.current_board = board
    self.ships_to_place = [(4, 1), (3, 2), (2, 3), (1, 4)]  # (длина, количество)
    self.current_ship_index = 0
    self.horizontal = True
    title = tk.Label(
        self.window,
        text=f"{player_name}, расставьте корабли",
        font=("Arial", 16)
    )
    title.pack(pady=10)
    self.ship_info_label = tk.Label(self.window, text="", font=("Arial", 12))
    self.ship_info_label.pack()
    self.update_ship_info()
    rotate_btn = tk.Button(
        self.window,
        text="Повернуть (R)",
        command=self.rotate_ship
    )
    rotate_btn.pack(pady=5)
    frame, self.placement_canvas = self.create_field_canvas(
        self.window,
        "Ваше поле",
        clickable=True,
        click_callback=self.place_ship_click
    )
    frame.pack(pady=10)
    auto_btn = tk.Button(
        self.window,
        text="Расставить автоматически",
        command=lambda: self.auto_place(on_complete)
    )
    auto_btn.pack(pady=5)
    self.on_placement_complete = on_complete
    self.draw_field(self.placement_canvas, board.get_field_for_display())
def update_ship_info(self):
    """Обновить информацию о текущем корабле"""
    if self.current_ship_index < len(self.ships_to_place):
        length, count = self.ships_to_place[self.current_ship_index]
        direction = "горизонтально" if self.horizontal else "вертикально"
        self.ship_info_label.config(
            text=f"Корабль: {length} клетки, осталось: {count}, направление: {direction}"
        )
def rotate_ship(self):
    """Повернуть корабль"""
    self.horizontal = not self.horizontal
    self.update_ship_info()
def place_ship_click(self, x, y):
    """Обработка клика при расстановке"""
    if self.current_ship_index >= len(self.ships_to_place):
        return
    length, count = self.ships_to_place[self.current_ship_index]
    if self.current_board.place_ship(x, y, length, self.horizontal):
        self.ships_to_place[self.current_ship_index] = (length, count - 1)
        if count - 1 == 0:
            self.current_ship_index += 1
        self.draw_field(self.placement_canvas, self.current_board.get_field_for_display())
        self.update_ship_info()
        if self.current_ship_index >= len(self.ships_to_place):
            self.window.after(500, self.on_placement_complete)
def auto_place(self, on_complete):
    """Автоматическая расстановка"""
    self.current_board.__init__()
    self.current_board.place_ships_randomly()
    self.draw_field(self.placement_canvas, self.current_board.get_field_for_display())
    self.window.after(500, on_complete)
def setup_game_screen(self, game, player1_name, player2_name):
    """Экран игры"""
    for widget in self.window.winfo_children():
        widget.destroy()
    self.game = game
    self.turn_label = tk.Label(self.window, text="", font=("Arial", 14))
    self.turn_label.pack(pady=10)
    fields_frame = tk.Frame(self.window)
    fields_frame.pack()
    frame1, self.enemy_canvas = self.create_field_canvas(
        fields_frame,
        "Поле противника",
        clickable=True,
        click_callback=self.shoot_click
    )
    frame1.pack(side=tk.LEFT, padx=20)
    frame2, self.my_canvas = self.create_field_canvas(
        fields_frame,
        "Ваше поле",
        clickable=False
    )
    frame2.pack(side=tk.LEFT, padx=20)
    self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
    self.result_label.pack(pady=10)
    self.update_game_display()
def update_game_display(self):
    """Обновить отображение игры"""
    if self.game.current_player == 1:
        self.turn_label.config(text="Ход: Игрок 1")
        enemy_field = self.game.board2.get_field_for_display(hide_ships=True)
        my_field = self.game.board1.get_field_for_display()
    else:
        self.turn_label.config(text="Ход: Игрок 2")
        enemy_field = self.game.board1.get_field_for_display(hide_ships=True)
        my_field = self.game.board2.get_field_for_display()
    self.draw_field(self.enemy_canvas, enemy_field)
    self.draw_field(self.my_canvas, my_field)
def shoot_click(self, x, y):
    """Обработка выстрела"""
    result = self.game.make_shot(x, y)
    messages = {
        "miss": "Мимо!",
        "hit": "Попадание!",
        "destroy": "Корабль уничтожен!",
        "win": "ПОБЕДА!",
        "invalid": "Сюда уже стреляли!"
    }
    self.result_label.config(text=messages.get(result, ""))
    if result == "win":
        winner = f"Игрок {self.game.winner}"
        self.show_winner(winner)
    else:
        self.update_game_display()
def show_winner(self, winner):
    """Показать победителя"""
    for widget in self.window.winfo_children():
        widget.destroy()
    label = tk.Label(
        self.window,
        text=f"Победил {winner}!",
        font=("Arial", 24)
    )
    label.pack(pady=50)
    btn = tk.Button(
        self.window,
        text="В главное меню",
        font=("Arial", 14),
        command=self.setup_main_menu
    )

    btn.pack()
def start_vs_friend(self):
    """Начать игру с другом"""
    from game_modes import TwoPlayerGame
    self.game = TwoPlayerGame()
    self.setup_placement_screen(
        "Игрок 1",
        self.game.board1,
        self.player1_ready
    )
def player1_ready(self):
    """Игрок 1 закончил расстановку"""
    self.game.setup_phase_complete(1)
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

