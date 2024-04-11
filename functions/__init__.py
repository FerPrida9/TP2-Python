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

def influence (players):
    """ esta funcion recibe el diccionario de jugadores y crea una lista
    de tuplas que contiene 2 elementos: nombre y la suma total del valor
    de cada estadistica"""
    return [(player, stats[0]*1.5 + stats[1]*1.25 + stats[2]) for player, stats in players.items()]

def most_influential (players):
    """ esta funcion recibe el diccionario de jugadores, crea la lista de 
    tuplas con la funcion influence, y en base a esa lista calcula el
    jugador/jugadora mas influyente y retorna su nombre"""
    influence_list = influence (players)
    best_player = max (influence_list, key = lambda x: x[1])
    return best_player[0]
    
def goal_average (goals):
    """ esta funcion recibe la lista de goles y retorna el 
    promedio de goles por partido del equipo"""
    return sum(goals)/25

def goalscorer_average (goal_scorer):
    """ esta funcion recibe la tupla con los datos del goleador/goleadora
    y retorna el promedio de goles por partido de ese jugador/jugadora"""
    return goal_scorer[1]/25 
    



    

         


