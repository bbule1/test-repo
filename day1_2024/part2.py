if __name__ == "__main__":
    input_file = 'input_file.txt'

    left_list = []
    right_list = []

    with open(input_file) as f:
        for i in f.readlines():
            two_out = i.split()
            left_list.append(int(two_out[0]))
            right_list.append(int(two_out[1]))

    similarity_list = [i * right_list.count(i) for i in left_list]

    print(str(sum(similarity_list)))