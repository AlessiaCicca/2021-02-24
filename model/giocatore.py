from dataclasses import dataclass

@dataclass
class Giocatore:
    PlayerID:int
    Name:str
    efficienza:int
    squadra:int


    def __hash__(self):
        return hash(self.PlayerID)

    def __str__(self):
        return f"{self.PlayerID} - {self.Name}"