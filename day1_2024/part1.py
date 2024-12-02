if __name__ == "__main__":
    input_file = 'input_file.txt'

    left_list = []
    right_list = []

    with open(input_file) as f:
        for i in f.readlines():
            two_out = i.split()
            left_list.append(int(two_out[0]))
            right_list.append(int(two_out[1]))

    left_list.sort()
    right_list.sort()
    print(left_list)

    diff_list = []

    for a, b in zip(left_list, right_list):
        diff_list.append(abs(a-b))

    print(str(sum(diff_list)))