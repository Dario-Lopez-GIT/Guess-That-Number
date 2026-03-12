import random


def get_limit():
    """Handles the level selection without a while loop."""
    try:
        user_input = input("\nChoose your level (100, 250, or 500): ")
        limit = int(user_input)
        if limit not in [100, 250, 500]:
            print("Invalid choice. Defaulting to 100.")
            return 100
        return limit
    except ValueError:
        print("Invalid input. Defaulting to 100.")
        return 100


def play_round(target, limit, attempts, max_attempts):
    """Recursive function to handle the 10 guessing attempts."""
    if attempts >= max_attempts:
        print("\nO" + ("~" * 10) + "x")
        print("BOOM! The bomb has gone off and you lost the game!")
        print(f"The hidden number was: {target}")
        return 0  # Return a score of 0 for a loss

    # Visual Fuse Logic
    fuse_remaining = max_attempts - attempts
    print(f"\nFuse: O{'~' * (fuse_remaining - 1)}  {'~' * attempts}x")

    try:
        guess = int(input(f"Attempt {attempts + 1}/10 - Guess (1-{limit}): "))
        diff = abs(target - guess)

        if guess == target:
            score = 100 - (10 * attempts)
            print(f"The Bomb has been DEFUSED! Correct Number found on {attempts + 1} guesses.")
            print(f"Your Score: {score} points")
            return score

        # Feedback logic
        if diff <= 3:
            print("-> You almost have it!")
        elif diff <= 10:
            print("-> The Number is close!")
        elif diff <= 30:
            print("-> Getting Close.")
        elif diff <= 75:
            print("-> Not even close.")
        else:
            print("-> Way off, Are You EVEN TRYING?")

    except ValueError:
        print("Invalid input. The fuse is still burning...")

    return play_round(target, limit, attempts + 1, max_attempts)


def game_loop(high_score=0):
    """Main recursive loop to handle game restarts."""
    limit = get_limit()
    target = random.randint(1, limit)

    current_score = play_round(target, limit, 0, 10)
    new_high_score = max(high_score, current_score)

    print(f"Current High Score: {new_high_score}")

    if input("\nDo you want to play again? (yes/no): ").lower() == 'yes':
        game_loop(new_high_score)
    else:
        print("Goodbye, Hero!")


def play_game():
    print("=" * 30)
    print("WELCOME TO BOMB DEFUSER")
    print("You have 10 chances to guess the correct number before the bomb explodes.")
    print("=" * 30)
    game_loop()


if __name__ == "__main__":
    play_game()
