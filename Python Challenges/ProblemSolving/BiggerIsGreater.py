def biggerIsGreater(w):
    pivot = -1
    for f in range(len(w)-2, -1, -1):
        if w[f] < w[f+1]:
            pivot = f
            break

    if pivot > -1:
        for f in range( pivot+1, len(w)):
            if w[pivot] < w[f]:
                swap = f
        w = w[:pivot] + w[swap] + w[pivot+1:swap] + w[pivot] + w[swap+1:]
        w = w[:pivot+1] + "".join(sorted(w[pivot+1:]))
        return w

    return "no answer"

if __name__ == '__main__':
    # w = "hefg"
    # w = "bb"
    w = "dkhc"
    # w = "zyyxwwtrrnmlggfeb"
    result = biggerIsGreater(w)
    print(result)
