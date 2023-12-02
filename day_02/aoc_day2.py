import re

with open("input.txt") as file:
    lines = [re.split("; |: ", line.rstrip()) for line in file]

# Part 1

games = []

for l in lines:
    game_dict = {}
    for game in l[1:]:  # ignore the first element because first game is showing "Game X"
        for g in game.split(", "):
            if g[g.find(" ")+1] not in game_dict.keys():  # check if the cube color is in the game_dict already
                game_dict[g[g.find(" ")+1]] = int(g[:g.find(" ")])  # if cube color not in dict, add the cube value in dict
            elif int(g[:g.find(" ")]) > game_dict[g[g.find(" ")+1]]:  # only update if cube value is larger than before
                game_dict[g[g.find(" ")+1]] = int(g[:g.find(" ")])
    games.append(game_dict)

real_games = 0
idx = 1
for i in games:
    if not (i['b'] > 14 or i['r'] > 12 or i['g'] > 13):
        real_games += idx
    idx += 1

print("Answer to Part 1 is: {}".format(real_games))

# Part 2:

max_games = []

for l in lines:
    game_dict = {}
    for game in l[1:]:
        for g in game.split(", "):
            if g[g.find(" ")+1] not in game_dict.keys():
                game_dict[g[g.find(" ")+1]] = int(g[:g.find(" ")])
            elif int(g[:g.find(" ")]) > game_dict[g[g.find(" ")+1]]:
                game_dict[g[g.find(" ")+1]] = int(g[:g.find(" ")])
    max_games.append(game_dict)

power_games = 0
for i in max_games:
    power_games += i['b'] * i['r'] * i['g']

print("Answer to Part 2 is: {}".format(power_games))