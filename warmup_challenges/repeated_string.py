def repeatedString(s, n):
    count = s.count("a")
    return round(n / len(s) * count)


if __name__ == "__main__":
    s = "aba"
    n = 10
    result = repeatedString(s, n)
    print(result)
