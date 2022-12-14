L = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
player = 'x'
player_1 = player

def endOfGame():
    global L

    for i in range(3):
        first = L[i][0]
        if first == '-':
            continue
        result = True
        for j in range(3):
            if L[i][j] != first:
                result = False
                break
        if result:
            return True

    for j in range(3):
        first = L[0][j]
        if first == '-':
            continue
        result = True
        for i in range(3):
            if L[i][j] != first:
                result = False
                break
        if result:
            return True

    first = L[0][0]
    if first != '-':
        result = True
        for i in range(3):

            if L[i][i] != first:
                result = False
                break
        if result:
            return True

    first = L[0][2]
    if first != '-':
        result = True
        for i in range(3):
            if L[2 - i][i] != first:
                result = False
                break
        if result:
            return True

    return False


def printGame():
    for row in L:
        print(*row)


while not endOfGame():
    printGame()
    player_1 = player
    i, j = int(input('Введите значение i: ')), int(input('Введите значение j: '))

    while L[i][j] != '-':
        i, j = int(input('Введите корректное значение i: ')), int(
            input('Введите корректное значение j: '))

    L[i][j] = player
    player = 'o' if player == 'x' else 'x'

printGame()
print(f"{player_1*4} TADA {player_1*4}")

