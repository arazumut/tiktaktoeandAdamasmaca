class Tablero:
    def __init__(self):
        self.celdas = [
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0]
        print(self.celdas)
    
    def draw(self):
        print(f"""\t _______________________
\t|       |       |       |
\t|   {self.celdas[6]}   |   {self.celdas[7]}   |   {self.celdas[8]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.celdas[3]}   |   {self.celdas[4]}   |   {self.celdas[5]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.celdas[0]}   |   {self.celdas[1]}   |   {self.celdas[2]}   |
\t|_______|_______|_______|""")


class Jugador:
    def __init__(self, jugador):
        print("__init__ Jugador")
        self.jugador = jugador


class Juego:
    def __init__(self):
        print("__init__ Juego")
        self.tablero = Tablero()
        self.jugadores = [
            Jugador('X'),
            Jugador('O')
        ]

    def jugar(self):
        self.tablero.draw()


juego = Juego()
juego.jugar()