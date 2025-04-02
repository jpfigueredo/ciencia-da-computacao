def selection_sort(players):
    n = len(players)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if players[j][1] > players[max_index][1]:
                max_index = j
        players[i], players[max_index] = players[max_index], players[i]
    return players

players = [
    ("Alice", 120),
    ("Bob", 90),
    ("Charlie", 150),
    ("Diana", 110), 
]

sorted_players = selection_sort(players)
print("Jogadores ordenados por pontuação:")
for name, score in sorted_players:
    print(f"{name}: {score}")
