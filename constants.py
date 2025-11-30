# =Правила Интерфейса=
# Размер поля
FIELD_SIZE = 10
# Корабли: {размер: количество}
SHIPS = {4: 1, 3: 2, 2: 3, 1: 4}

# Состояния 
EMPTY = 0 # Пусто
SHIP = 1 # Корабль
MISS = 2 # Промах
HIT = 3 # Попадание
DESTROYED = 4 # Уничтожен

# Результаты выстрела
RESULT_MISS = "miss"
RESULT_HIT = "hit"
RESULT_DESTROY = "destroy"
RESULT_WIN = "win"
RESULT_INVALID = "invalid" # Уже стреляли сюда
