def generate(inp, factor):
    return (inp * factor) % 2147483647

if __name__ == '__main__':
    A, B, count = 277, 349, 0
    for i in range(5000000):
        while A % 4:
            A = generate(A, 16807)
        while B % 8:
            B = generate(B, 48271)
        low_a16 = str(format(A, '032b'))[-16:]
        low_b16 = str(format(B, '032b'))[-16:]
        if low_a16 == low_b16 and not A % 4 and not B % 8:
            count += 1

        A = generate(A, 16807)
        B = generate(B, 48271)
    print(count)