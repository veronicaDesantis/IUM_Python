from django.contrib import admin
from .models import Game
from .models import Move

admin.site.register(Game)
admin.site.register(Move)