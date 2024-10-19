import random


def get_computer_choice(items):
    """
    Select one at random from the items
    """
    return random.choice(items)


def get_user_choice(items):
    """
    Get user choice
    """
    print('Input index to make your choice:')
    for index, item in enumerate(items, start=1):
        print(f'index: {index}, item: {item}')

    try:
        user_input = int(input())
        if user_input not in range(1, len(items) + 1):
            print('Invalid input. Please try again.')
            return get_user_choice(items)
        return items[user_input - 1]
    except ValueError:
        print('Invalid input. Please enter a number.')
        return get_user_choice(items)


def determine_winner(u_choice, c_choice):
    """
    Determine the winner based on choices
    """
    if u_choice == c_choice:
        return None  # Tie
    if (u_choice == "wizard" and c_choice == "warrior") or \
            (u_choice == "warrior" and c_choice == "rogue") or \
            (u_choice == "rogue" and c_choice == "wizard"):
        return "User"
    return "Computer"


def main():
    items = ['wizard', 'warrior', 'rogue']
    print('Welcome to the Wizard, Warrior, Rogue Tournament!')
    print('Compete against the computer. First to win 3 rounds is the champion!')

    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        u_choice = get_user_choice(items)
        c_choice = get_computer_choice(items)
        print(f'User Choice: {u_choice} and Computer Choice: {c_choice}.')

        winner = determine_winner(u_choice, c_choice)

        if winner == "User":
            user_score += 1
            print('You win this round!')
        elif winner == "Computer":
            computer_score += 1
            print('Computer wins this round!')
        else:
            print('It is a tie, continue to the next round...')

        print(f'Score - You: {user_score}, Computer: {computer_score}')
        print('---')

    print(f'Final Score - You: {user_score}, Computer: {computer_score}')

    if user_score > computer_score:
        print('Congratulations! You are the champion!')
    else:
        print('The computer wins! Better luck next time!')


if __name__ == '__main__':
    main()