def play_game():
    frames = []

    for i in range(10):
        print('Frame', i + 1)
        first_attempt = int(input('  >>> first throw? '))
        if first_attempt < 10:
            second_attempt = int(input('  >>> second throw? '))
            frames[i] = [first_attempt, second_attempt]
        else:
            frames.append([first_attempt])

    print(frames)


if __name__ == "__main__":
    play_game()
