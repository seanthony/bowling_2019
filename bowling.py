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


def get_throw(attempt, n, frame):
    while True:
        throw = input(f'  >>> throw #{attempt}? ')
        if not throw.isdigit():
            # non digit entries
            print('err - non numeric')
            continue
        throw_value = int(throw)
        if throw_value > 10 or throw_value < 0:
            # invalid throw values
            print('err - throw value out of bounds')
            continue
        if n < 10 and throw_value + sum(frame) > 10:
            # all non tenth frames going over ten
            print('err - value too high for frame')
            continue
        if n == 10 and len(frame) == 1 and frame[0] < 10 and frame[0] + throw_value > 10:
            # tenth frame, not strike on first ball
            print('err - second throw too high for frame')
            continue
        if n == 10 and len(frame) == 2 and frame[0] == 10 and frame[1] < 10 and throw_value + frame[1] > 10:
            # tenth frame, strike on first ball, non-strike on second, final throw
            print('err - third throw too high for frame')
            continue
        return throw_value


def bowl(n):
    print('Frame', n)
    frame = []
    throw = get_throw(1, n, frame)
    frame.append(throw)
    if sum(frame) < 10 or n == 10:
        throw = get_throw(2, n, frame)
        frame.append(throw)
    if sum(frame) >= 10 and n == 10:
        throw = get_throw(3, n, frame)
        frame.append(throw)

    return frame


def play_game():
    frames = []
    for i in range(10):
        frame = bowl(i + 1)
        frames.append(frame)

    print(frames)
    score = score_game(frames)
    print("Final Score:", score)


if __name__ == "__main__":
    play_game()
