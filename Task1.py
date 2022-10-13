def list_to_int(list_input):
    int_output = 0
    list_len = len(list_input)
    for num in list_input:
        list_len -= 1
        int_output += num * pow(10, list_len)
    print(int_output)


list1 = [8, 3, 5, 1]
list_to_int(list1)
