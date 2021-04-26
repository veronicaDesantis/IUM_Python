from .list_models import GameList
from .detail_models import MoveDetail
from .detail_models import GameDetail
from .enum import PointValue, StatusType
from .query_manager import get_game
from .query_manager import get_move_by_all
from .query_manager import get_last_move
from .query_manager import update_game
from .query_manager import update_game_status


def GameListFactory(game):
    game_list = []
    for g in game:
        str_date = g.dateStart.strftime('%m/%d/%Y')
        str_date_update = g.dateLastUpdate.strftime('%m/%d/%Y')
        game_list.append(GameList(_id=g.id, player1point=g.player1point, player2point=g.player2point, status=g.status,
                                  dateStart=str_date, dateLastUpdate=str_date_update))
    return game_list


def GameFactory(_id):
    game = get_game(_id)
    matrix = []
    for r in range(0, game.nRighe):
        sub_matrix = []
        for c in range(0, game.nColonne):
            db_correspondent = get_move_by_all(indexRow=r, indexColumn=c, game_id=game.id)
            if db_correspondent:
                sub_matrix.append(MoveDetail(player_type=db_correspondent[0].playerType, nRighe=r, nColonne=c))
            else:
                sub_matrix.append(MoveDetail(player_type=0, nRighe=r, nColonne=c))
        matrix.append(sub_matrix)
    # verify the last move
    move_to = get_last_move(game_id=game.id)
    move_to_int = 1
    if move_to:
        if move_to.playerType:
            if move_to.playerType == 1:
                move_to_int = 2
            else:
                move_to_int = 1
    game.player1point = PointFactory(nRows=game.nRighe, nColumn=game.nColonne, player_type=1, matrix=matrix)
    game.player2point = PointFactory(nRows=game.nRighe, nColumn=game.nColonne, player_type=2, matrix=matrix)
    game_detail = GameDetail(id=_id, player1point=game.player1point, player2point=game.player2point,
                             nColonne=game.nColonne, nRighe=game.nRighe, matrix=matrix, move_to=move_to_int)
    update_game(_id=game.id, player1point=game.player1point, player2point=game.player2point)
    if game.player1point >= int(PointValue.FIFTY_POINT):
        game_detail.wonBy = 1
        game_detail.isFinished = 1
        # update the db entity
        update_game_status(_id=_id, status=int(StatusType.WON_BY_PLAYER_1))
        game_detail.move_to = 0
    elif game.player2point >= int(PointValue.FIFTY_POINT):
        game_detail.wonBy = 2
        game_detail.isFinished = 1
        # update the db entity
        update_game_status(_id=_id, status=int(StatusType.WON_BY_PLAYER_2))
        game_detail.move_to = 0
    return game_detail


def PointFactory(nRows, nColumn, player_type, matrix):
    point = 0
    series = 0
    # explore the length
    for r in range(0, nRows):
        for c in range(0, nColumn):
            if matrix[r][c].player_type == player_type:
                series = series + 1
            else:
                point = point + CalculatePoint(series=series)
                series = 0
        point = point + CalculatePoint(series=series)
        series = 0
    series = 0
    # explore the height
    for c in range(0, nColumn):
        for r in range(0, nRows):
            if matrix[r][c].player_type == player_type:
                series = series + 1
            else:
                point = point + CalculatePoint(series=series)
                series = 0
        point = point + CalculatePoint(series=series)
        series = 0
    series = 0
    # explore the diagonals from back to top
    # start from -nRows and ignore the negative value
    for c in range(-nRows, nColumn):
        for r in range(0, nRows):
            _sum = r + c
            if _sum >= 0:
                if _sum < nColumn:
                    cell = matrix[r][_sum]
                    if cell.player_type == player_type:
                        series = series + 1
                    else:
                        point = point + CalculatePoint(series=series)
                        series = 0
        point = point + CalculatePoint(series=series)
        series = 0
    series = 0
    # explore the diagonals from top to back
    # start from -nRows and ignore the negative value
    nRows_nColumns = nRows + nColumn
    for c in range(nRows_nColumns, 0, -1):
        for r in range(0, nRows):
            delta = c - r
            if delta >= 0:
                if delta < nColumn:
                    cell = matrix[r][delta]
                    if cell.player_type == player_type:
                        series = series + 1
                    else:
                        point = point + CalculatePoint(series=series)
                        series = 0
        point = point + CalculatePoint(series=series)
        series = 0
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
