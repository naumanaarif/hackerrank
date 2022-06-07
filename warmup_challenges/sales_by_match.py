def sockMerchant(n, arr):
    pairs = {}
    for i in range(n):
        key = arr[i]
        if key not in pairs:
            pairs[key] = arr.count(key)
    
    pair_count = 0
    for pair in pairs:
        pair_count += pairs[pair] // 2
    return pair_count


if __name__ == '__main__':
    pile = [1, 2, 1, 2, 1, 3, 2]
    n = len(pile)
    pairs = sockMerchant(n, pile)
    print(pairs)
