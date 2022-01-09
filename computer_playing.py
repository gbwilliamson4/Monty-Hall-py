import random

swapWins = 0
swapLosses = 0
stayWins = 0
stayLosses = 0

total_plays = 100000000

for i in range(total_plays):
    # Pick door with car
    doorThatHasCar = random.randint(1, 3)

    # choose random door
    doorPick = random.randint(1, 3)

    # Open a door that doesnt have the car
    while True:
        # Select a door that is a goat and not picked by the player
        showGoatDoor = random.randint(1, 3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break

    if i <= (total_plays / 2):
        swap = 'Y'
    else:
        swap = 'N'

    # Swap the players door if they wanted to swap
    if swap == 'Y':
        if doorPick == 1 and showGoatDoor == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2
        elif doorPick == 2 and showGoatDoor == 1:
            doorPick = 3
        elif doorPick == 2 and showGoatDoor == 3:
            doorPick = 1
        elif doorPick == 3 and showGoatDoor == 1:
            doorPick = 2
        elif doorPick == 3 and showGoatDoor == 2:
            doorPick = 1

    if doorPick == doorThatHasCar:
        # print("You won!")
        if swap == 'Y':
            swapWins += 1
        elif swap == 'N':
            stayWins += 1
    else:
        # print('Sorry, you lost.')
        if swap == 'Y':
            swapLosses += 1
        elif swap == 'N':
            stayLosses += 1

    # Calculate success rate of swapping and not swapping:
    totalSwaps = swapWins + swapLosses
    if totalSwaps != 0:  # Prevent divide by 0 error
        swapSuccess = round(swapWins / totalSwaps * 100, 1)
    else:
        swapSuccess = 0.0

    totalStays = stayWins + stayLosses
    if (stayWins + stayLosses) != 0:
        staySuccess = round(stayWins / totalStays * 100, 1)
    else:
        staySuccess = 0.0

    print(i)

print()
print('Swapping:   ', end='')
print('{} wins, {} losses, '.format(swapWins, swapLosses), end='')
print('success rate {}%'.format(swapSuccess))
print('Not swapping: ', end='')
print('{} wins, {} losses, '.format(stayWins, stayLosses), end='')
print('success rate {}%'.format(staySuccess))

# 500 swaps
# 500 stays
# compare differences
