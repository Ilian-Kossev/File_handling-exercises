def count_letters_and_punctuation_signs(string):
    counter_chars = 0
    counter_punctuation_signs = 0
    for ch in string:
        if ch.isalpha():
            counter_chars += 1
        elif ch == ' ':
            continue
        elif ch.isnumeric():
            continue
        else:
            counter_punctuation_signs += 1
    return counter_chars, counter_punctuation_signs


with open('source.txt') as file:
    counter = 0
    for line in file:
        counter += 1
        new_line = f'Line {counter}: {line.strip()} ({count_letters_and_punctuation_signs(line)[0]}) ({count_letters_and_punctuation_signs(line.strip())[1]})'
        with open('result.txt', 'a') as result_file:
            result_file.write(new_line)
            result_file.write('\n')

