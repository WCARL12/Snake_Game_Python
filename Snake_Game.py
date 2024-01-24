import random
import time

# Ask the user if they want to know the rules
def introduction():
        rules_choice = ''
        continue_choice = ''
        print(f"SNAKE GAME!")
        time.sleep(2)

        while rules_choice != 'yes' and rules_choice != 'no':

            rules_choice = input("Do you want to see the rules? (yes/no): ")

            if rules_choice != 'yes' and rules_choice != 'no':
                print("Sorry please try again and type your choice as either 'yes' or 'no'\n")

        if rules_choice == 'yes':
            snake_rules()

            while continue_choice != 'yes':
                continue_choice = input((f'Continue: (yes/no): '))

# Displays the rules
def snake_rules():
    print(f"""
    1.) The Snake game is a game of risks! 
    2.) There are 5 rounds/ 5 letters in 'SNAKE'.
    3.) The SNAKE game uses 2 dice which is a 6 sided dice.
    3.) If ONE of the die rolls to 1 you will lose all your points in that round.
    4.) But if BOTH dice rolls to 1 you will lose every points you accumulated so far in all of the rounds (SNAKE EYES!).
    2.) Both players can either risk their points or to stop.
    6.) Once a player stops risking, their turn is done for the rest of that round and their points is accumulated.
    7.) The player that risks their points can still roll until they stop or get a 1 in one of the die.
    8.) The player with the most amount of points in the end wins!
          
_____________________________________________________________________________________________________         
|          |      S      |      N      |      A      |      K      |      E      |      Total       |
|__________|_____________|_____________|_____________|_____________|_____________|__________________|
|Player_1: |      0      |      0      |     0       |      0      |      0      |        0         |
|          |             |             |             |             |             |                  |
|Player_2: |      0      |      0      |     0       |      0      |      0      |        0         |
|__________|_____________|_____________|_____________|_____________|_____________|__________________|  

""")

# Display the scores for the snake board

def display_scores(player_1_total, player_2_total, player_1_all_total, player_2_all_total):
    s_1 = player_1_total[0]
    n_1 = player_1_total[1]
    a_1 = player_1_total[2]
    k_1 = player_1_total[3]
    e_1 = player_1_total[4]
    t_1 = player_1_all_total

    s_2 = player_2_total[0]
    n_2 = player_2_total[1]
    a_2 = player_2_total[2]
    k_2 = player_2_total[3]
    e_2 = player_2_total[4]
    t_2 = player_2_all_total

    print(f"""
    _____________________________________________________________________________________________________         
    |          |      S      |      N      |      A      |      K      |      E      |      Total       |
    |__________|_____________|_____________|_____________|_____________|_____________|__________________|
    |Player_1: |     {s_1:<7} |     {n_1:<7} |     {a_1:<7} |     {k_1:<7} |     {e_1:<7} |       {t_1:<10} |
    |          |             |             |             |             |             |                  |
    |Player_2: |     {s_2:<7} |     {n_2:<7} |     {a_2:<7} |     {k_2:<7} |     {e_2:<7} |       {t_2:<10} |
    |__________|_____________|_____________|_____________|_____________|_____________|__________________|  
    """)


# This pops the empty strings in the list of scores of a player and replace it with the recent score
def player_round_list(player_round_total, player_all_total, board_counter):

    player_all_total.pop(board_counter)
    player_all_total.insert(board_counter, player_round_total)
    return player_all_total

    
# Gets the dice number
def die_roll():
    die = random.randint(1, 6)
    return die


# Display the 2 dices 
def display_dice(dice_roll):
    print(f"\nDie 1: {dice_roll[0]}")
    time.sleep(1.5)
    print(f"Die 2: {dice_roll[1]}")
    time.sleep(1.5)


# Display the conditions if 1 die rolls to 1 or both rolls to 1
def display_conditions(dice_roll, player):
    if dice_roll[0] == 1 and dice_roll[1] == 1:
        print("\nSnake Eyes!")
        time.sleep(3)
        print("You lost all your points accumulated so far in all of the rounds.")
        time.sleep(4)
        print(f"Player {player} turn has ended for this round.")
        time.sleep(4)
    
    elif dice_roll[0] == 1 or dice_roll[1] == 1:
        print("\nOne of the dices rolls to 1")
        time.sleep(3)
        print(f'Your round score is set to 0.')
        time.sleep(4)
        print(f"Your turn has ended for this round.")
        time.sleep(4)


# Function if one of the roll is 1
def counter_conditions(counter, dice_roll, num):
    if counter == num and 1 not in dice_roll:
        counter += 1
    return counter


def dice_conditions(dice_roll, player_total):
    # The turn variable is a way to assign a roll if it's snake eyes or one of the roll is a 1
    # Turn = 1 is snake eyes
    # Turn = 2  is one of the roll is 1 
    if dice_roll[0] == 1 and dice_roll[1] == 1:
        player_total = 0
        turn = 1 #  Both dice rolls to 1 
    elif dice_roll[0] == 1 or dice_roll[1] == 1:
        player_total = 0
        turn = 2 # One of the dice rolls to 1
    else:
        score = sum(dice_roll)
        player_total += score
        turn = 0 # None of the die rolls to 1
    return turn, player_total

# This function asks the player if they want to risk or not
def turn_conditions(turn, player):
    # if turn == 1 and turn == 2 this assigns a player a choice automatically because they got snakes eyes or 1 in their roll to make them stop rolling the dice

    if turn == 0:
        player_choice = ''
        while True:
            print('================================')
            player_choice = input(f"Player {player} roll again? (risk/stop): ")
            if player_choice == 'stop':
                turn = 2
                break
            elif player_choice == 'risk':
                break
            elif player_choice != 'stop' and player_choice != 'risk':
                print("Sorry please try again\n")

    elif turn == 1 or turn == 2:
        player_choice = 'stop'
    
    return player_choice, turn

#This funcition will change all the scores to 0 if both dice rolls to 1
def snake_change_display(player_turn, player_total, round_num):
    if player_turn == 1 :
        for x in range(round_num):
            player_total.pop(x)
            player_total.insert(x, 0)
    return player_total


# Changes the player total to 0 
def snake_total(turn, player_total):
    if turn == 1:
        player_total = 0
    return player_total


#Function that displays who the winner
def winner(player_1_all_total, player_2_all_total):
    if player_1_all_total > player_2_all_total:
        print("Player 1 wins!")
    elif player_1_all_total < player_2_all_total:
        print("Player 2 wins!")
    else:
        print("It's a tie")

def main():
    player_1_all_total = 0
    player_2_all_total = 0
    counter = 0 # Variable to keep rolling if the first roll is 1
    board_counter = -1 # For asking the user to continue until round 5

    # This varible is for displaying the scores
    display_player_1_board = ['', '', '', '', '']
    display_player_2_board = ['', '', '', '', '']

    introduction()

    # There are 5 rounds/5 letters in 'SNAKE'
    for x in range(5):
        # Variables needed to work and resets when a turn is done
        player_1_turn = 0
        player_2_turn = 0
        player_1_choice = ''
        player_2_choice = ''
        player_1_round_total = 0
        player_2_round_total = 0
        player_1 = 1 # Knowing which player
        player_2 = 2 # Knowing which player
        letter = 'SNAKE' 
        counter = 0 
        continue_choice = ''

        print(f"\nRound {letter[x]} will now begin!")
        time.sleep(1)

        # The round will keep going until both players stopped
        while player_1_choice != 'stop' or player_2_choice != 'stop':
            
            # Player 1 turn
            if (player_1_turn != 1 or player_1_turn != 2) and player_1_choice != 'stop':
                while True:
                    dice_roll = [die_roll(), die_roll()] # get the dice number

                    counter = counter_conditions(counter, dice_roll, num=0) # Rolls again when there is a 1 on the first roll

                    print('================================\n')
                    print("(Player 1 rolls the dice...)")
                    time.sleep(2)

                    display_dice(dice_roll) # displays the dice
            
                    if counter == 0:
                        print('\nRestart again, there is 1 in the first roll')
                        time.sleep(3)
                        continue
                    else:
                        break

                display_conditions(dice_roll, player_1)
            

            # This will determine if a player can still roll or not depending on what number the dice landed
            if player_1_choice != 'stop':
                player_1_turn, player_1_round_total = dice_conditions(dice_roll, player_1_round_total)


            # Player 2 turn this time
            if (player_2_turn != 1 or player_2_turn != 2) and player_2_choice != 'stop':
                while True:

                    dice_roll = [die_roll(), die_roll()] # get the dice number
                    counter = counter_conditions(counter, dice_roll, num=1) # Rolls again when there is a 1 on the first roll

                    print('================================\n')

                    print("(Player 2 rolls the dice...)")
                    
                    time.sleep(1.5)

                    display_dice(dice_roll) # displays the dice
            
                    if counter == 1:
                        print('\nRestart again, there is 1 in the first roll')
                        time.sleep(3)
                        continue
                    else:
                        break

                display_conditions(dice_roll, player_2)

            if player_2_choice != 'stop':
                player_2_turn, player_2_round_total = dice_conditions(dice_roll, player_2_round_total)
            
            print('================================\n')
            time.sleep(2)
            print(f'Player_1 round "{letter[x]}" current total is: {player_1_round_total}')
            print(f'Player_2 round "{letter[x]}" current total is: {player_2_round_total}\n')

            # Asks the players if they want to roll depending on the player_turn
            player_1_choice, player_1_turn = turn_conditions(player_1_turn, player_1)
            player_2_choice, player_2_turn = turn_conditions(player_2_turn, player_2)

        board_counter += 1
        time.sleep(2)
        print(f'\nRound {letter[x]} final scores: '),
        time.sleep(2)

        # Calculates the scores
        player_round_list(player_1_round_total, display_player_1_board, board_counter)
        display_player_1_board = snake_change_display(player_1_turn, display_player_1_board, x)
        player_round_list(player_2_round_total, display_player_2_board, board_counter)
        display_player_2_board = snake_change_display(player_2_turn, display_player_2_board, x)

        player_1_all_total += player_1_round_total
        player_1_all_total = snake_total(player_1_turn, player_1_all_total)
        player_2_all_total += player_2_round_total
        player_2_all_total = snake_total(player_2_turn, player_2_all_total)
        display_scores(display_player_1_board, display_player_2_board, player_1_all_total, player_2_all_total)
        print('================================')

        # Asks the user if they want to continue after the score board has been displayed
        if board_counter != 4:
            while continue_choice.lower() != "yes":
                continue_choice = input("Continue? (yes/no): ")
            print("================================")
    winner(player_1_all_total, player_2_all_total)
    print("================================")

if __name__ == "__main__":
    main()
