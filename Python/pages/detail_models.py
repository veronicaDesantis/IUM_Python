
class GameDetail():
    id = int
    nRighe = int
    nColonne = int
    player1point = int
    player2point = int
    matrix = []
    move_to = int
    isFinished = bool
    wonBy = int
    percentage = int

    def __init__(self, id, player1point, player2point, nColonne, nRighe, matrix, move_to):
        self.player1point = player1point
        self.player2point = player2point
        self.id = id
        self.nColonne = nColonne
        self.nRighe = nRighe
        self.matrix = matrix
        self.move_to = move_to
        self.isFinished = 0
        self.wonBy = 0
        self.percentage = 100 / self.nColonne




class MoveDetail():
    player_type = int
    nRighe = int
    nColonne = int
    cValue = str

    def __init__(self, player_type, nRighe, nColonne):
        self.player_type = player_type
        self.nRighe = nRighe
        self.nColonne = nColonne
        if self.player_type == 0:
            self.cValue = "player_none"
        elif self.player_type == 1:
            self.cValue = "player_one"
        elif self.player_type == 2:
            self.cValue = "player_two"
