def checksum(filename):
    c_sum = 0
    with open(filename) as f:
        rows = f.readlines()
        for row in rows:
            elements = list(row.rstrip().split('\t'))
            flag = False

            for i in range(len(elements)):
                if flag:
                    break

                for j in range(i + 1, len(elements)):
                    if flag:
                        break

                    biggest = int(elements[i])
                    smallest = int(elements[j])
                    if biggest < smallest:
                        biggest, smallest = smallest, biggest
                    if not biggest % smallest:
                        c_sum += biggest / smallest
                        flag = True

    return c_sum

if __name__ == "__main__":
    print(checksum('day2.txt'))