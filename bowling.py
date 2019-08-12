def score_game(frames):
    # not accurate bowling scoring!
    score = 0
    for frame in frames:
        score += sum(frame)

    return score


def play_game():
    frames = []

    for i in range(10):
        print('Frame', i + 1)
        first_attempt = int(input('  >>> first throw? '))
        if first_attempt < 10:
            second_attempt = int(input('  >>> second throw? '))
            frames.append([first_attempt, second_attempt])
        else:
            frames.append([first_attempt])

    print(frames)
    score = score_game(frames)
    print("Score:", score)


if __name__ == "__main__":
    play_game()
