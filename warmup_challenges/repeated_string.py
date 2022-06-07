def repeatedString(s, n):
    count = s.count("a")
    count = n // len(s) * count
    remaining_count = s[: n % len(s)].count("a")
    return count + remaining_count


if __name__ == "__main__":
    s = "aba"
    n = 10
    result = repeatedString(s, n)
    print(result)
