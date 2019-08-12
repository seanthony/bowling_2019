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
            else:
                score += sum(frames[i + 1])
        elif sum(frame) == 10:
            score += frames[i + 1][0]
        scores.append(score)

    # last frame
    scores.append(sum(frames[-1]))

    print(scores)
    return sum(scores)


def bowl(n):
    print('Frame', n)
    frame = []
    throw = int(input('  >>> first throw? '))
    frame.append(throw)
    if sum(frame) < 10 or n == 10:
        throw = int(input('  >>> second throw? '))
        frame.append(throw)
    if sum(frame) >= 10 and n == 10:
        throw = int(input('  >>> third throw? '))
        frame.append(throw)

    return frame


def play_game():
    frames = []
    for i in range(10):
        frame = bowl(i + 1)
        frames.append(frame)
        # score = score_game(frames)
        # print("Score:", score)

    print(frames)
    score = score_game(frames)
    print("Final Score:", score)


if __name__ == "__main__":
    play_game()
