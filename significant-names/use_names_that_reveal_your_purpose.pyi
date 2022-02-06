#BAD CODE
#   Não indica nenhuma ideia.
d = ""

#GOOD CODE
# Indica claramente a ideia, valor e como é mensurado o valor da variável.
elapsed_time_in_days = 0
days_since_creation = 0
days_since_modification = 0
file_age_in_days = 0

#BAD CODE
# O que está dentro de the_list?
# Qual a importancia da posição zero na the_list?
# Qual a importầncia do valor 4?
# Como eu usuaria a lista retornada?
def get_them() -> list:
    list1 = []
    the_list = [[1,2,3],[4,2]]
    for x in the_list:
        if x[0] == 4:
            list1.append(x)
    return list1

#AVERAGE CODE
# Dessa forma é possível identificar que estamos trabalhados com algo parecido com "campo minado"
# Cada quadrado é representado por um vetor simples e que a posiução zero armazena o status.
# O valor 4 significa marcado com a bandeira.
STATUS_VALUE = 0
FLAGGED = 4
def get_flagged_cells() -> list:
    flagged_cells = []
    game_board = [[1,2,3],[4,2]]
    for cell in game_board:
        if cell[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(cell)
    return flagged_cells

#GOOD CODE
# É interessante criar uma classe simples para lidar com as celulas no lugar da lista, contendo uma função
# chamada is_flagged para ocultar os números mágicos.

class Cell:
    def __init__(self, cell: list):
        self.status_value = 0
        self.flagged = 4
        self.cell = cell

    def is_flagged(self):
        if self.cell[self.status_value] == self.flagged:
            return True
        return False


def get_flagged_cells() -> list:
    flagged_cells = []
    game_board = [Cell(cell=[1,2,3]), Cell(cell=[1,2,3])]
    for cell in game_board:
        if cell.is_flagged():
            flagged_cells.append(cell)
    return flagged_cells
