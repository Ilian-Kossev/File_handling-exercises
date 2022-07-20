def replace_symbols(sentence):
    new_str = ''
    for char in sentence:
        if char in {"-", ",", ".", "!", "?"}:
            char = '@'
        new_str += char
    return new_str


def reverse_lines(sentence):
    list_sentence = sentence.split(' ')
    reversed_sentence = reversed(list_sentence)
    return ' '.join(reversed_sentence)


with open('text.txt') as file:
    counter = 0
    for line in file:
        if counter % 2 == 0:
            string = replace_symbols(line).strip()
            reversed_string = reverse_lines(string)
            print(reversed_string)

        counter += 1

