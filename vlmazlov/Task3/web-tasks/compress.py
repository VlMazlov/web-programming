__author__ = 'vlmazlov'

def compress(sequence):

    compressed_sequence = []
    index = 0

    while index < len(sequence):
        current_value_num = 0
        current_value = sequence[index]

        #do while loop:
        while True:
            current_value_num += 1
            index += 1

            if index >= len(sequence):
                break

            next_value = sequence[index]

            if current_value != next_value:
                break

        compressed_sequence.append((current_value_num, current_value))

    return compressed_sequence

def decompress(sequence):

    decompressed_sequence = []

    for pair in sequence:
        entries_num, value = pair
        decompressed_sequence.extend([value for i in range(entries_num)])

    return decompressed_sequence

compressed_sequence = compress(input().split())
print(compressed_sequence)
print(decompress(compressed_sequence))

