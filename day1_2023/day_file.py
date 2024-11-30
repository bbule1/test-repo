if __name__ == "__main__":
    import re

    input_file = 'input_file.txt'

    with open(input_file) as f:
        list_of_digit = []

        for word in f.read().splitlines():
            output = re.findall(r'\d', word)
            final_digit = output[0] + output[-1]
            final_int = int(final_digit)
            list_of_digit.append(final_int)

        print(sum(list_of_digit))








