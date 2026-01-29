def are_arrays_equal(a, b):
    if len(a) != len(b):
        return False

    count = [0] * 11  # since values range from 0 to 10

    for x in a:
        count[x] += 1

    for x in b:
        count[x] -= 1

    for c in count:
        if c != 0:
            return False

    return True
