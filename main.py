def residual(x, y):
    i = 0
    while not (x < y):
        x -= y
        i += 1
    return i, x


def division(x, y):
    a, b = residual(x, y)
    value = f"{a}."
    i = 0
    while b:
        if i == 15:
            break
        k = "10"
        l = len(str(b)) - len(str(y))
        for _ in range(l):
            k += "0"
        k = int(k)
        a, b = residual(b * k, y)
        value += str(a)
        i += 1
    return float(value)


if __name__ == '__main__':
    r = division(100, 3)
    print(r)
