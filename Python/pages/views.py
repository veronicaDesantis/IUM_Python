import datetime

from django.shortcuts import render, redirect
from .models import Game
from .models import Move
from .enum import StatusType
from .list_models import GameList
from .factory import GameFactory

def home_view(request, *args, **kwargs):
    game = Game.objects.filter(status=int(StatusType.INITIATED))
    game_list = []
    for g in game:
        str_date = g.dateStart.strftime('%m/%d/%Y')
        str_date_update =g.dateLastUpdate.strftime('%m/%d/%Y')
        game_list.append(GameList(player1point=g.player1point, player2point=g.player2point, status=StatusType(g.status), dateStart=str_date, dateLastUpdate=str_date_update))
    context = {'game_list': game_list}
    if request.POST:
        nRighe = request.POST['nRighe']
        nColonne = request.POST['nColonne']
        game = Game(nRighe=nRighe, nColonne=nColonne, dateStart=datetime.date.today(), dateLastUpdate=datetime.date.today(), player1point=0, player2point=0, status=int(StatusType.INITIATED))
        game.save()
        return redirect('game_view', id=game.id)
    return render(request, "home_template.html", context)

def game_view(request, id, *args, **kwargs):
    context = {'game_detail' :  GameFactory(id)}
    return render(request, "game_view.html",context)

def game_view_post(request, *args, **kwargs):
    #inserisco la mossa
    id = request.POST["game_id"]
    index_row = request.POST["index_row"]
    index_column = request.POST["index_column"]
    move_to = request.POST["move_to"]
    game_ = Game.objects.filter(id=id).first()
    move = Move(game=game_, indexRighe=index_row, indexColonne=index_column, playerType=move_to)
    move.save()
    #verifico se il blocco inserito è vicino ad altri e sulla base di quello aggiungo punti
    context = {'game_detail': GameFactory(id)}
    return render(request, "game_view.html", context)