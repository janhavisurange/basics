import random 
print('''
__________.__                 __        ____.              __    
\______   \  | _____    ____ |  | __   |    |____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /   |    \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    </\__|    |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \________(____  /\___  >__|_ \
        \/          \/            \/             \/     \/     \/
''')
print("WELCOME TO BLACKJACK\n")

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
class dealer:
    def __init__(self):
        self.dlrcards = []

class player:
    def __init__(self):
        self.plcards = []


def compare():
    if sum(dlr1.dlrcards) > 21 and sum(pl1.plcards) < 21:
        print(f'Dealer total: {sum(dlr1.dlrcards)}\nPlayer total: {sum(pl1.plcards)}')
        print('Dealer busted. You win!')
    elif sum(dlr1.dlrcards) < 21 and sum(pl1.plcards) > 21:
        print(f'Dealer total: {sum(dlr1.dlrcards)}\nPlayer total: {sum(pl1.plcards)}')
        print('Its a bust. You lost.')
    elif sum(dlr1.dlrcards) == sum(pl1.plcards):
        print(f'Dealer total: {sum(dlr1.dlrcards)}\nPlayer total: {sum(pl1.plcards)}')
        print('Its a tie. ')
    elif sum(dlr1.dlrcards) < 21 and sum(pl1.plcards) < 21:
        if sum(dlr1.dlrcards) > sum(pl1.plcards):
            print(f'Dealer total: {sum(dlr1.dlrcards)}\nPlayer total: {sum(pl1.plcards)}')
            print('Dealer won. You lost.')
        else:
            print(f'Dealer total: {sum(dlr1.dlrcards)}\nPlayer total: {sum(pl1.plcards)}')
            print('Dealer lost. You win!')
    

def stand():
    print('Dealer: ', end='')
    for i in dlr1.dlrcards:
        print(f'{i}, ', end = '')
    print(f'Total = {sum(dlr1.dlrcards)}')

    if sum(dlr1.dlrcards) < 17:
        print('hitting card for dealer...')
        while sum(dlr1.dlrcards) < 17:
            dlr1.dlrcards.append(random.choice(cards))
            while sum(dlr1.dlrcards) > 21 and 11 in dlr1.dlrcards:
                dlr1.dlrcards[dlr1.dlrcards.index(11)] = 1
        print('New dealer cards: ', end='')
        for i in dlr1.dlrcards:
            print(f'{i} ', end='')
    
    compare()

choice = 'y'
while choice.lower() == 'y':
    dlr1 = dealer()
    dlr1.dlrcards.append(random.choice(cards))
    dlr1.dlrcards.append(random.choice(cards))
    while sum(dlr1.dlrcards) > 21 and 11 in dlr1.dlrcards:
        dlr1.dlrcards[dlr1.dlrcards.index(11)] = 1
    print(f"Dealer: x, {dlr1.dlrcards[1]}")

    pl1 = player()
    for i in range(2):
        pl1.plcards.append(random.choice(cards))
        while sum(pl1.plcards) > 21 and 11 in pl1.plcards:
            pl1.plcards[pl1.plcards.index(11)] = 1

    print(f"Player: {pl1.plcards[0]}, {pl1.plcards[1]}")
    print(f'Total: {sum(pl1.plcards)}')
    if sum(pl1.plcards) == 21:
        print('You win!! ')
        choice = input('Wanna play another round? Type y for yes, n for no\n')


    flag = True
    while flag == True:
        move = input("Do you want to hit or stand? Type h for hit or s for stand\n")


        if move.lower() == 'h':
            pl1.plcards.append(random.choice(cards))
            while sum(pl1.plcards) > 21 and 11 in pl1.plcards:
                pl1.plcards[pl1.plcards.index(11)] = 1
            print('Player: ',end='')
            for i in pl1.plcards:
                print(f'{i}, ', end='')
            if sum(pl1.plcards) > 21:
                flag = False
                print(f'\nOops! Your sum went overboard. Total: {sum(pl1.plcards)}')
                if sum(pl1.plcards) == sum(dlr1.dlrcards):
                    print(f'Dealer also has total {sum(dlr1.dlrcards)}. Its a tie.')
                else:
                    print(f'Dealer had {sum(dlr1.dlrcards)}. You lost.')
            if sum(pl1.plcards) < 21:
                pass 

        if move.lower() == 's':
            flag = False
            stand()
    choice = input('Wanna play another round? Type y for yes, n for no\n')


