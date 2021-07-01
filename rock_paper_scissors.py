from random import randint

def player(options):
    j=-1
    for i in options:
        j=j+1
        print("{}={}".format(j,i))
        
    player_choice = int(input('What do you choose?'))
    return player_choice


def system(content):
    length=len(content)-1
    system_choice = randint(0,length)
    return system_choice
    

def check(choices, player, system):
    if player == system:
        print("It's a Tie")
    # Condition 1: Player chose Rock and System chose Scissors
    # Condition 2: Player chose Paper and System chose Rock or Player chose Scissors and System chose Paper
    # Condition 3: Player didn't choose Scissors when System chose Rock
    elif (player == 0 and system == len(choices)-1) or (player>system and not(player==len(choices)-1 and system==0)):
        print("Player Won")
        return
    else:
        print("Player lost")


def play():
    print('''
    ---------------------------------
    Welcome to the game of Rock, Paper, Scissors.
    Please choose your weapon
    ''')

    choices = ['Rock', 'Paper' , 'Scissors']
    player_result = player(choices)
    system_result = system(choices)
    
    #Choises of both player and system
    print("Player chose {}".format(choices[player_result]))
    print("System chose {}".format(choices[system_result]))
    
    #Function to check and print the winner.
    check(choices,player_result,system_result)
    #print (f'\n{results}')

def main():

    #force the player into the play loop
    play_again = ''
    while play_again.lower() != 'n':
        play()
        print ("\nDo you want to play again?")
        play_again = input('type \'y\' for yes or \'n\' for no: ')

main()
