def allUnique(sub):
    seen = []
    for i in sub:
        if i in seen:
            return False
        seen.append(i)

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "c"
    w = len(a)
    subs = []
    for i in range(len(a)):
        w = len(a) - i
        while w > 0:
            sub = ''
            for k in range(i, i + w):
                sub += a[k]

            subs.append(sub)
            w = w - 1

    max_len = 0
    for sub in subs:
        if allUnique(sub):
            max_len = max(max_len, len(sub))

    print(max_len)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
