def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(len(weights)):
        cache[weights[i]] = i
    for i in range(len(weights)):
        dif = limit - weights[i]
        if dif in cache:
            return (max(i, cache[dif]), min(i, cache[dif]))

    return None
