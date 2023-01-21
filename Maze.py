import random
# field
width, height = 20, 10 #Розмір поля гри.
playerX, playerY = 0, 0 #Початкова позиція гравця.


def init(field):
    global playerX, playerY
    playerX, playerY = place_character()
    finishX, finishY = place_character()
    field[finishY][finishX] = 'F'


def create_field(block_frequency): # Створення поля для гри.
    field = [[]] #Ініціалізація двовимірного масиву.
    for i in range(height): #Цикл щоб пройтись по height.
        field.append([])  #Заповнення массива по height пустими значеннями.
        for j in range(width): #Цикл щоб пройтись по width.
            symbol_to_place = '.' #Символ по якому ми можемо ходити.
            random_number = random.randint(0, 100) #Рандом числа від 0 до 100.
            if random_number < block_frequency: 
                symbol_to_place = '#'
            field[i].append(symbol_to_place)

    return field


def place_character(): #Спавн гравця в рандомному місці.
    x = random.randint(0, width)
    y = random.randint(0, height)
    return x, y


def draw_field(field):
    for i in range(height):
        for j in range(width):
            symbol_to_draw = field[i][j]
            if playerX == j and playerY == i:
                symbol_to_draw = '@'
            print(symbol_to_draw, end='')
        print()


def is_end_game(field):
    return field[playerY][playerX] == 'F'


def get_input():
    str = input() #Вводимо якесь значення.
    direction = str[0]  # 'W'/'A'/'S'/'D'
    dx, dy = 0, 0

    if direction == 'W':
        dy = -1
    elif direction == 'A':
        dx = -1
    elif direction == 'S':
        dy = +1
    elif direction == 'D':
        dx = +1

    return dx, dy


def can_move(field, newX, newY):
    return newX < width and newY < height and newX >= 0 and newY >= 0 and field[newY][newX] != '#'


def move(newX, newY):
    global playerX, playerY
    playerX, playerY = newX, newY


def try_move(field, dx, dy):
    newX = playerX + dx
    newY = playerY + dy
    if can_move(field, newX, newY):
        move(newX, newY)


def logic(field, dx, dy):
    try_move(field, dx, dy)


def main():
    field = create_field(20)
    init(field)
    #Поле з решітками і крапками. Кінцевий пункт призначення.

    while not is_end_game(field):
        draw_field(field)
        dx, dy = get_input()
        logic(field, dx, dy)

main()
