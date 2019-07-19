from random import choice

players = []
file = open('players.txt' , 'r')
players = file.read().splitlines()

teamA =[]
teamB=[]
print('players : ' , players)

while len(players) > 0 :
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice (players)
    teamB.append (playerB)
    players.remove(playerB)

print('team A : ' ,teamA)
print('team B : ' ,teamB)
