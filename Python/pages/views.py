import datetime

from django.shortcuts import render, redirect

from .enum import StatusType
from .factory import GameFactory
from .factory import GameListFactory
from .query_manager import get_all_game_list
from .query_manager import insert_game
from .query_manager import update_game_status
from .query_manager import insert_move
from .query_manager import get_game


def home_view(request, *args, **kwargs):
    game = get_all_game_list()
    game_list = GameListFactory(game)
    context = {'game_list': game_list}
    if request.POST:
        nRow = request.POST['nRighe']
        nColumns = request.POST['nColonne']
        _id = insert_game(nRow, nColumns, datetime, datetime)
        return redirect('game_view', _id=_id)
    return render(request, "home_template.html", context)


def game_view(request, _id, *args, **kwargs):
    context = {'game_detail': GameFactory(_id)}
    return render(request, "game_view.html", context)


def game_view_post(request, *args, **kwargs):
    # insert the move
    _id = request.POST["game_id"]
    index_row = request.POST["index_row"]
    index_column = request.POST["index_column"]
    move_to = request.POST["move_to"]
    game_ = get_game(_id)
    insert_move(game=game_, index_row=index_row, index_column=index_column, move_to=move_to)
    return redirect('game_view', _id=_id)


def leave_1(request, *args, **kwargs):
    _id = request.POST["game_id"]
    update_game_status(_id=_id, status=int(StatusType.LEAVED_BY_PLAYER_1))
    return redirect('game_view', _id=_id)


def leave_2(request, *args, **kwargs):
    _id = request.POST["game_id"]
    update_game_status(_id=_id, status=int(StatusType.LEAVED_BY_PLAYER_2))
    return redirect('game_view', _id=_id)
