class Giocatore(object):
    def __init__(self, nickname="", punti=0):
        self.nickname = nickname
        self.punti = punti

    def __str__(self):
        return f'{self.nickname} {self.punti}'