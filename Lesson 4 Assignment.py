from random import randrange as rr


def get_weapon():
    print("1 rock\n2 paper\n3 scissor")
    pick = int(input("Pick your weapon:"))
    return pick

def opponent():
    pick = rr(1,3)
    return pick

def result(player1,player2):
    if  player1 == player2:
        print("Draw!")
        return
    elif player1 == 1:
        if player2 == 3:
            print("You win!")
        else:
            print("You lose!")
    elif player1 == 2:
        if player2 == 1:
            print("You win!")
        else:
            print("You lose!")
    elif player1 == 3:
        if player2 == 2:
            print("You win!")
        else:
            print("You lose!")
    return

def matchup(player1,player2):
    if player1 == 1:
        one = "Rock"
    elif player1 == 2:
        one = "Paper"
    else:
        one = "Scissor"
    if player2 == 1:
        two = "Rock"
    elif player2 == 2:
        two = "Paper"
    else:
        two = "Scissor"
    print(f"{one} vs. {two}!")

def main():
    keep_playing = "y"
    while keep_playing.lower() == 'y':
        print("===================")
        weapon = get_weapon()
        op_weapon = opponent()
        matchup(weapon,op_weapon)
        result(weapon,op_weapon)
        keep_playing = input("keep playing? (y/n)")
    return

if __name__ == '__main__':
    main()

print("Completed by James Light")