from django.db import models


class Game(models.Model):
    nRighe = models.IntegerField()
    nColonne = models.IntegerField()
    player1point = models.IntegerField()
    player2point = models.IntegerField()
    status = models.IntegerField()
    dateStart = models.DateTimeField()
    dateLastUpdate = models.DateTimeField()


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    indexRighe = models.IntegerField()
    indexColonne = models.IntegerField()
    playerType = models.IntegerField()
