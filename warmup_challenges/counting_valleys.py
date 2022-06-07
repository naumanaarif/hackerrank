

def countingValleys(steps, path):
    sea_level, valleys = 0, 0
    for i in range(steps):
        prev_step = sea_level
        step_up, step_down = path[i] == 'U', path[i] == 'D'
        if step_up:
            sea_level += 1
        elif step_down:
            sea_level -= 1
        next_step = sea_level

        if prev_step == 0 and next_step == -1:
            valleys += 1
    return valleys


if __name__ == '__main__':
    path = "UDDDUDUU"
    steps = len(path)
    valleys = countingValleys(steps, path)
    print(valleys)
