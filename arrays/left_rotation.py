def rotate_left(arr: list, d: int) -> list:
    return arr[d:] + arr[:d]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    result = rotate_left(a, 4)
    print(result)
