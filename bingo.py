import random

def bingo_game():
    print("Welcome to the Bingo Game!")

    player_numbers = random.sample(range(1, 50), 7)
    print(f"Your numbers: {player_numbers}")

    pulled_numbers = []  
    drawn_numbers = []   
    reward= [0, 1, 2, 5, 10, 100, 1000, 50000]  
    multiplier = 1  

    while len(drawn_numbers) < 7:
        new_number = random.randint(1, 49)
        if new_number not in pulled_numbers:
            pulled_numbers.append(new_number)
            drawn_numbers.append(new_number)
            print(f"Pulled number: {new_number}")

    print(f"Bingo numbers drawn: {drawn_numbers}")

    matches = set(player_numbers) & set(drawn_numbers)
    num_matches = len(matches)

    if matches:
        print(f"You matched {num_matches} number(s): {matches}")

        base_reward = reward[num_matches]

        for match in matches:
            if match % 7 == 0:
                print(f"Multiplier activated! Matched number {match} is divisible by 7.")
                multiplier *= 2

        total_reward = base_reward * multiplier
        print(f"Base reward: ${base_reward}")
        print(f"Multiplier applied: x{multiplier}")
        print(f"Total winnings: ${total_reward}")
    else:
        print("No matches this time. Better luck next time!")

bingo_game()
