#Import contains functions that will allow you to pick players randomly from a list
import random
#list is assigned to the variable players
players = ["Martin","Craig", "sue" ,"Claire","dave","alice","luciana","harry","jack","rose","lexi","maria","Thomas","James","William","ada","grace","jean","marissa","alan"]

print("welcome to team allocator")
#shuffle the list of players
#while true:
random.shuffle (players)

#Pick teams
team1 = players[:len(players)//2] #new list will be assigned to the variable team1
#select team capt
print("Team 1 captain: "+ random.choice(team1))
#display team1
print("team1: ")
for player in team1: # loop through team1
    print(player) # print current players name

 #Pick team2
team2 = players[:len(players)//2] #new list will be assigned to the variable team1
#select team capt
print("\nTeam 2 captain: "+ random.choice(team2))
#display team2
print("team2: ")
for player in team2: # loop through team1
    print(player) # print current players name

