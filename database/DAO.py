from database.DB_connect import DBConnect
from model.giocatore import Giocatore


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getMatch():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """select m.MatchID as id, t1.Name as s1, t2.Name as s2
from matches m, teams t1, teams t2
where m.TeamHomeID = t1.TeamID and m.TeamAwayID =t2.TeamID
order by m.MatchID"""

        cursor.execute(query)

        for row in cursor:
            result[f"[{row["id"]}] {row["s1"]} vs. {row["s2"]}"]=row["id"]

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(matchid):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.*, round((a.TotalSuccessfulPassesAll+a.Assists)/a.TimePlayed,3) as efficienza, a.TeamID  as squadra
from players p , actions a 
where p.PlayerID =a.PlayerID 
and a.MatchID=%s"""

        cursor.execute(query,(matchid,))

        for row in cursor:
            result.append(Giocatore(**row))

        cursor.close()
        conn.close()
        return result
