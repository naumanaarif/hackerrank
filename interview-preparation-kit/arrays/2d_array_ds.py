def hourglass_sum(array: list) -> int:
    max_sum = -99

    # Iterate through 4x4 mid array
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[0]) - 1):
            top = sum(array[i - 1][j - 1 : j + 2])
            mid = array[i][j]
            btm = sum(array[i + 1][j - 1 : j + 2])

            hourglass_sum = top + mid + btm
            max_sum = max(hourglass_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    array = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]

    result = hourglass_sum(array)
    print(result)
