def find_longest_chain(words):
    word_chain_lengths = {}

    for word in words:
        word_chain_lengths[word] = 1
    sorted_words = sorted(words, key=len)

    for word in sorted_words:
        for i in range(len(word)):
            word_without_el = word[:i] + word[i+1:]
            if word_without_el in word_chain_lengths:
                word_chain_lengths[word] = word_chain_lengths[word_without_el] + 1

    return max(word_chain_lengths.values())


def read_file_from_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

        if not lines:
            return "The file has no words"

        n = int(lines[0].strip())
        words = [line.strip() for line in lines[1:n + 1]]
    return words


def result_file(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))