from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: str

    def __str__(self):
        return f'{self.nome} ({self.codins})'
