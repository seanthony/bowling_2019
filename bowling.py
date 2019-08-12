def score_game(frames):
    scores = []
    for i in range(len(frames) - 1):
        frame = frames[i]
        score = sum(frame)
        if len(frame) == 1 and sum(frame) == 10:
            if (len(frames[i + 1]) > 1):
                score += sum(frames[i + 1][:2])
            elif len(frames) > (i + 2):
                score += frames[i + 1][0] + frames[i + 2][0]
        elif sum(frame) == 10:
            score += frames[i + 1][0]
        scores.append(score)

    scores.append(sum(frames[-1]))

    print(scores)
    return sum(scores)


def play_game():
    frames = []

    for i in range(9):
        print('Frame', i + 1)
        first_attempt = int(input('  >>> first throw? '))
        if first_attempt < 10:
            second_attempt = int(input('  >>> second throw? '))
            frames.append([first_attempt, second_attempt])
        else:
            frames.append([first_attempt])
        print("score:", score_game(frames))

    print('Frame 10')
    first_attempt = int(input('  >>> first throw? '))
    if first_attempt < 10:
        second_attempt = int(input('  >>> second throw? '))
        if first_attempt + second_attempt == 10:
            third_attempt = int(input('  >>> third throw? '))
            frames.append([first_attempt, second_attempt, third_attempt])
        else:
            frames.append([first_attempt, second_attempt])
    else:
        second_attempt = int(input('  >>> second throw? '))
        third_attempt = int(input('  >>> third throw? '))
        frames.append([first_attempt, second_attempt, third_attempt])

    print(frames)
    score = score_game(frames)
    print("Score:", score)


if __name__ == "__main__":
    play_game()
