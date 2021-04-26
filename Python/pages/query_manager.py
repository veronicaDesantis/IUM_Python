import datetime

from Python.pages.enum import StatusType
from Python.pages.models import Game, Move


def get_all_game_list():
    return Game.objects.all()


def get_game(_id):
    return Game.objects.filter(id=_id).first()


def insert_game(nRow, nColumns, dateStart, dateLastUpdate):
    game = Game(nRighe=nRow, nColonne=nColumns, dateStart=dateStart.date.today(),
                dateLastUpdate=dateLastUpdate.date.today(),
                player1point=0, player2point=0, status=int(StatusType.INITIATED))
    game.save()
    return game.id


def update_game(_id, player1point, player2point):
    game = get_game(_id)
    game.player1point = player1point
    game.player2point = player2point
    game.save()


def update_game_last_date(_id, dateLastUpdate):
    game = get_game(_id)
    game.dateLastUpdate = dateLastUpdate.date.today()
    game.save()


def update_game_status(_id, status):
    game = get_game(_id)
    game.status = status
    game.save()


def get_move_by_all(indexRow, indexColumn, game_id):
    return Move.objects.filter(indexRighe=indexRow, indexColonne=indexColumn, game_id=game_id)


def get_last_move(game_id):
    return Move.objects.filter(game_id=game_id).last()


def insert_move(game, index_row, index_column, move_to):
    move = Move(game=game, indexRighe=index_row, indexColonne=index_column, playerType=move_to)
    move.save()
    update_game_last_date(game.id, datetime)
