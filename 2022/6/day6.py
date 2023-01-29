with open('day6.txt', 'r') as file:
    buffer = file.readline().strip('\n')


def find_datastream(buffer, unique_count):
    buffer_len = len(buffer)
    for i in range(0, buffer_len):
        segment = buffer[i:i+unique_count]
        char_count = set(segment)
        if len(char_count) > unique_count-1:
            return i+unique_count


print(find_datastream(buffer, 4))
print(find_datastream(buffer, 14))
