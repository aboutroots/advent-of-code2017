def single_hash(lengths, pos, skip, a_list):
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
        if skip_size > len(a_list) - 1:
            skip_size = skip_size % len(a_list)

    return a_list[:], position, skip_size, a_list


def knot_hash(sequence):
    _ascii = [int(ord(c)) for c in ",".join(str(x) for x in sequence)]
    _ascii.extend([17, 31, 73, 47, 23])
    print(_ascii)
    sparse_hash, position, skip_size = list(range(256)), 0, 0
    for i in range(64):
        sparse_hash, position, skip_size, a_list = \
            single_hash(_ascii, pos=position, skip=skip_size,
                        a_list=sparse_hash)
    dense_hash = []
    for k in range(16):
        block = sparse_hash[16 * k:16 * k + 16]
        xor_result = block[0]
        for j in range(1, 16):
            xor_result ^= block[j]
        dense_hash.append(xor_result)

    dense_hash = [hex(x).lstrip('0x') for x in dense_hash]
    for i in range(len(dense_hash)):
        if len(dense_hash[i]) == 1:
            dense_hash[i] = '0' + dense_hash[i]
        if dense_hash[i] == '':
            dense_hash[i] = '00'

    return "".join(dense_hash)



if __name__ == "__main__":
    print(knot_hash(['31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33']))
# 31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33