def jumpingOnClouds(c):
    i, jumps = 0, 0
    n = len(c)

    while i < n - 1:
        # Jump two clouds, if possible
        if i + 2 < n and c[i + 2] == 0:
            jumps += 1
            i += 2
        # else, Jump one cloud
        elif i + 1 < n and c[i + 1] == 0:
            jumps += 1
            i += 1
    return jumps


if __name__ == "__main__":
    c = [0, 0, 1, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print(result)
