list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

#решение, которое уже было
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

#моё решение
#first_team = list_players[::2]
#second_team = list_players[1::2]


print(first_team)
print(second_team)
