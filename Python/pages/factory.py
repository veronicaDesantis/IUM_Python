from .models import  Game
from .models import Move
from .detail_models import MoveDetail
from .detail_models import GameDetail
from .enum import PointValue

def GameFactory(id):
    game = Game.objects.filter(id=id).first()
    matrix = []
    for r in range(0, game.nRighe):
        sub_matrix = []
        for c in range(0, game.nColonne):
            db_correspondend = Move.objects.filter(indexRighe=r, indexColonne=c, game_id=id)
            if db_correspondend:
                sub_matrix.append(MoveDetail(player_type=db_correspondend[0].playerType, nRighe=r, nColonne=c))
            else:
                sub_matrix.append(MoveDetail(player_type=0, nRighe=r, nColonne=c))
        matrix.append(sub_matrix)
    # verifico di chi è stata l'ultima mossa
    move_to = Move.objects.filter(game_id=id).last()
    move_to_int = 1
    if move_to.playerType:
        if move_to.playerType == 1:
            move_to_int = 2
        else:
            move_to_int = 1
    print("Player 1")
    game.player1point = PointFactory(nRighe=game.nRighe, nColonne=game.nColonne, player_type=1, matrix=matrix)
    print("Player 2")
    game.player2point = PointFactory(nRighe=game.nRighe, nColonne=game.nColonne, player_type=2, matrix=matrix)
    game_detail = GameDetail(id=id, player1point=game.player1point, player2point=game.player2point,
                             nColonne=game.nColonne, nRighe=game.nRighe, matrix=matrix, move_to=move_to_int)
    return game_detail

def PointFactory(nRighe,nColonne, player_type, matrix):
    point = 0
    series = 0
    # explore the length
    for r in range(0, nRighe):
        for c in range(0, nColonne):
            if matrix[r][c].player_type == player_type:
                series = series + 1
            else:
                point = point + CalculatePoint(series=series)
                series = 0
    series = 0
    # explore the height
    for c in range(0, nColonne):
        for r in range(0, nRighe):
            if matrix[r][c].player_type == player_type:
                series = series + 1
            else:
                point = point + CalculatePoint(series=series)
                series = 0
    series = 0
    #explore the diagonals from back to top
    #start from -nRighe and ignore the negative value
    for c in range(-nRighe, nColonne):
        for r in range(0, nRighe):
            sum = r + c
            if sum >= 0:
                if sum < nColonne:
                    cell = matrix[r][sum]
                    if cell.player_type == player_type:
                        series = series + 1
                    else:
                        point = point + CalculatePoint(series=series)
                        series = 0
    series = 0
    # explore the diagonals from top to back
    # start from -nRighe and ignore the negative value
    nRighenColonne = nRighe + nColonne
    for c in range(nRighenColonne, 0, -1):
        for r in range(0, nRighe):
            delta = c - r
            if delta >= 0:
                if delta < nColonne:
                    print(str(r) + ":" + str(delta))
                    cell = matrix[r][delta]
                    if cell.player_type == player_type:
                        series = series + 1
                    else:
                        point = point + CalculatePoint(series=series)
                        series = 0
        print("change")
    return point


def CalculatePoint(series):
    if series == 5:
        return int(PointValue.FIFTY_POINT)
    elif series == 4:
        return int(PointValue.TEN_POINT)
    elif series == 3:
        return int(PointValue.TWO_POINT)
    else:
        return int(PointValue.ZERO_POINT)


