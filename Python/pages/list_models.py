from Python.pages.enum import StatusType


class GameList():
    _id = int
    player1point = int
    player2point = int
    status = int
    dateStart = str
    dateLastUpdate = str
    status_string = str
    href_btn = str
    src = str

    def __init__(self, _id, player1point, player2point, status, dateStart, dateLastUpdate):
        self._id = id
        self.player1point = player1point
        self.player2point = player2point
        self.status = status
        self.dateStart = dateStart
        self.dateLastUpdate = dateLastUpdate
        if self.status == int(StatusType.INITIATED):
            self.status_string = "In corso"
        elif self.status == int(StatusType.WON_BY_PLAYER_1):
            self.status_string = "Vinta dal Player 1"
        elif self.status == int(StatusType.WON_BY_PLAYER_2):
            self.status_string = "Vinta dal Player 2"
        elif self.status == int(StatusType.LEAVED_BY_PLAYER_1):
            self.status_string = "Abbandonata dal Player 1"
        elif self.status == int(StatusType.LEAVED_BY_PLAYER_2):
            self.status_string = "Abbandonata dal Player 2"
        self.src = "/game_view/" + str(_id)
