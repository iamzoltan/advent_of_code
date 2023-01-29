from functools import cmp_to_key


with open('day13.txt', 'r') as file:
    pairs = file.read().split('\n')


def compare_elems(left, right):
    if type(left) == int and type(right) == int:
        return left < right
    elif type(left) == list and type(right) == list:
        for i in range(len(left)):
            if i >= len(right):
                return False
            if compare_elems(left[i], right[i]):
                return True
            if compare_elems(right[i], left[i]):
                return False
            else: 
                continue
        if len(left) < len(right):
            return True
        return False
    elif type(left) == int and type(right) == list:
        return compare_elems([left], right)
    else:
        return compare_elems(left, [right])


def format_comp_for_functool(left, right):
    if compare_elems(left, right):
        return -1
    elif not compare_elems(left, right):
        return 1
    else:
        return 0


ind_sums = 0
decoder_key1 = 0
decoder_key2 = 0
packets = []
for i in range(0, len(pairs), 3):
    # part 1
    left_packet, right_packet = pairs[i:i+2]
    left, right = eval(left_packet), eval(right_packet)
    if compare_elems(left, right):
        ind_sums += i//3 + 1
    # part 2
    packets.append(left)
    packets.append(right)
print(ind_sums)


div1 = [[2]]
div2 = [[6]]
packets.append(div1)
packets.append(div2)
packets.sort(key=cmp_to_key(format_comp_for_functool))
for i, packet in enumerate(packets):
    if packet == [[2]]:
        decoder_key1 = i + 1
    elif packet == [[6]]:
        decoder_key2 = i + 1
print(decoder_key1, decoder_key2)
print(decoder_key1 * decoder_key2)

