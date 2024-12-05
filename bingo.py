import random

def bingo_game():
    print("Welcome to the Bingo Game!")

    player_numbers = random.sample(range(1, 50), 7)
    print(f"Your numbers: {player_numbers}")

    pulled_numbers = []  
    drawn_numbers = []   
    rewards = [1, 2, 5, 10, 100, 1000, 10000]  
    jackpot = 50000  

    while len(drawn_numbers) < 7:
        new_number = random.randint(1, 49)
        if new_number not in pulled_numbers:
            pulled_numbers.append(new_number)
            drawn_numbers.append(new_number)
            print(f"Pulled number: {new_number} (Total pulled: {pulled_numbers})")

    print(f"Bingo numbers drawn: {drawn_numbers}")

    matches = set(player_numbers) & set(drawn_numbers)
    num_matches = len(matches)
    if num_matches > 0:
        reward = rewards[num_matches - 1]
        print(f"You matched {num_matches} number(s): {matches}")
        print(f"Your reward is: ${reward}")

        if num_matches == 7:
            print("Congratulations! You hit the Jackpot!")
            reward += jackpot
        print(f"Total winnings: ${reward}")
    else:
        print("No matches this time. Better luck next time!")

bingo_game()
