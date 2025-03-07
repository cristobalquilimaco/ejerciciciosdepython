import random
import curses

# Definimos las piezas
PIEZAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[0, 1, 0], [1, 1, 1]]  # T
]

# Tamaño de la pantalla
ANCHO = 10
ALTO = 20

# Inicialización de la pantalla
def init_screen():
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.timeout(100)
    return stdscr

# Función para crear una nueva pieza
def nueva_pieza():
    return PIEZAS[random.randint(0, len(PIEZAS) - 1)]

# Función para dibujar el tablero
def dibujar_tablero(stdscr, tablero):
    for y in range(ALTO):
        for x in range(ANCHO):
            char = ' ' if tablero[y][x] == 0 else '#'
            stdscr.addstr(y, x * 2, char)

# Función para verificar si una pieza puede moverse
def colision(tablero, pieza, offset):
    x_offset, y_offset = offset
    for y, fila in enumerate(pieza):
        for x, val in enumerate(fila):
            if val:
                new_x = x + x_offset
                new_y = y + y_offset
                if new_x < 0 or new_x >= ANCHO or new_y >= ALTO or tablero[new_y][new_x]:
                    return True
    return False

# Función para agregar la pieza al tablero
def agregar_pieza(tablero, pieza, offset):
    x_offset, y_offset = offset
    for y, fila in enumerate(pieza):
        for x, val in enumerate(fila):
            if val:
                tablero[y + y_offset][x + x_offset] = val

# Función para eliminar filas completas
def eliminar_filas(tablero):
    new_tablero = [fila for fila in tablero if any(cell == 0 for cell in fila)]
    new_tablero = [[0] * ANCHO] * (ALTO - len(new_tablero)) + new_tablero
    return new_tablero

# Función principal del juego
def juego(stdscr):
    tablero = [[0] * ANCHO for _ in range(ALTO)]
    pieza = nueva_pieza()
    offset = [ANCHO // 2 - len(pieza[0]) // 2, 0]
    score = 0

    while True:
        stdscr.clear()
        dibujar_tablero(stdscr, tablero)
        stdscr.addstr(ALTO, 0, f"Score: {score}")
        stdscr.refresh()

        # Mover la pieza según la entrada
        tecla = stdscr.getch()

        if tecla == curses.KEY_RIGHT:
            nueva_pos = [offset[0] + 1, offset[1]]
            if not colision(tablero, pieza, nueva_pos):
                offset = nueva_pos
        elif tecla == curses.KEY_LEFT:
            nueva_pos = [offset[0] - 1, offset[1]]
            if not colision(tablero, pieza, nueva_pos):
                offset = nueva_pos
        elif tecla == curses.KEY_DOWN:
            nueva_pos = [offset[0], offset[1] + 1]
            if not colision(tablero, pieza, nueva_pos):
                offset = nueva_pos
            else:
                agregar_pieza(tablero, pieza, offset)
                tablero = eliminar_filas(tablero)
                pieza = nueva_pieza()
                offset = [ANCHO // 2 - len(pieza[0]) // 2, 0]
                score += 10

        # Verificar si la pieza toca el fondo
        if colision(tablero, pieza, [offset[0], offset[1] + 1]):
            agregar_pieza(tablero, pieza, offset)
            tablero = eliminar_filas(tablero)
            pieza = nueva_pieza()
            offset = [ANCHO // 2 - len(pieza[0]) // 2, 0]

        # Game Over
        if colision(tablero, pieza, offset):
            stdscr.clear()
            stdscr.addstr(ALTO // 2, ANCHO // 3, "GAME OVER")
            stdscr.refresh()
            stdscr.getch()
            break

        # Dibujar la pieza actual
        agregar_pieza(tablero, pieza, offset)

curses.wrapper(juego)
