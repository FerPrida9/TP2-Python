def estructura (names, goals, goals_avoided, assists):
    """ esta funcion recibe 4 listas y retorna un diccionario que tiene
    como llave los nombres de los jugadores y como valor una tupla de 
    3 elementos (goles, goles evitados, asistencias)"""
    players = {}
    for name, g, ga, a in zip(names, goals, goals_avoided, assists):
        players[name] = (g,ga,a)
    return players

def goal_scorer (players):
    """ esta funcion recibe el diccionario de jugadores y retorna una tupla
    con el nombre y los goles del goleador/goleadora"""
    max_goals = -1
    for player, values in players.items():
        if values[0] > max_goals:
            max_goals = values[0]
            max_player = player
    max = (max_player, max_goals)
    return max
    

         


