class GameList():
    player1point = int
    player2point = int
    status = str
    dateStart = str
    dateLastUpdate = str

    def __init__(self, player1point, player2point, status, dateStart, dateLastUpdate):
        self.player1point = player1point
        self.player2point = player2point
        self.status = status
        self.dateStart = dateStart
        self.dateLastUpdate = dateLastUpdate