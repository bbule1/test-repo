if __name__ == "__main__":
    list_of_word_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    list_of_key = list_of_word_num.keys()
    input_file = 'input_file.txt'
    min_len_num = 3

    with open(input_file) as f:
        list_of_digit = []
        for word in f.read().splitlines():
            first_digit = None
            word_builder_first = ''
            for letter in word:
                if first_digit is None:
                    if not letter.isdigit():
                        word_builder_first += letter
                        if min_len_num <= len(word_builder_first):
                            for key in list_of_key:
                                if word_builder_first.find(key) == -1:
                                    continue
                                else:
                                    first_digit = list_of_word_num.get(key)
                                    break

                    if letter.isdigit():
                        first_digit = letter
                        break



            last_digit = None
            word_builder_last = ''
            for letter in word[::-1]:
                if last_digit is None:
                    if not letter.isdigit():
                        word_builder_last += letter
                        if min_len_num <= len(word_builder_last):
                            for key in list_of_key:
                                if word_builder_last[::-1].find(key) == -1:
                                    continue
                                else:
                                    last_digit = list_of_word_num.get(key)
                                    break

                    if letter.isdigit():
                        last_digit = letter
                        break

            final_digit = first_digit + last_digit
            final_int = int(final_digit)
            list_of_digit.append(final_int)

            print(str(sum(list_of_digit)))









