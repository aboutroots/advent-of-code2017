def hash(lengths, pos, skip):
    a_list = list(range(256))
    position = pos
    skip_size = skip
    for l in lengths:
        # reverse
        if position + l - 1 < len(a_list):
            a_list[position:position + l] = a_list[position:position + l][::-1]
        else:
            re_position = position + l - len(a_list) - 1  # re-cycled index

            first_slice = a_list[position:]
            first_len = len(first_slice)
            second_slice = a_list[:re_position + 1]

            first_slice.extend(second_slice)
            first_slice[:] = first_slice[::-1]   # reverse

            a_list[position:] = first_slice[:first_len]
            a_list[:re_position + 1] = first_slice[first_len:]

        # position
        position += l + skip_size
        if position > len(a_list) - 1:
            position = position % len(a_list)
        skip_size += 1

    return a_list[:], position, skip_size

if __name__ == "__main__":
    h, p, s = hash([31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33], 0, 0)
    print(h[0] * h[1], p, s)