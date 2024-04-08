def estructura (names, goals, goals_avoided, assists):
    players = {}
    for name, g, ga, a in zip(names, goals, goals_avoided, assists):
        players[name] = (g,ga,a)
    return players