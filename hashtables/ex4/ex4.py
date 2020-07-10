def has_negatives(a):
    cache = {}
    results = []
    for i in a:
        cache[i] = i
        if i != 0 and -i in cache:
            results.append(abs(i))

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
