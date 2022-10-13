"""
Programming Task #1
Given a list of digits, determine the integer that it represents. 

For example, given the list: [8,3,5,1], your program should output 8351.

Note: You are not allowed to use conversion / casting functions, (i.e., str or int).

"""


def list_to_int(list_input):
    """Convert the list of digits into integer and print out.

    Args:
        list of digits
    """
    int_output = 0
    list_len = len(list_input)
    for num in list_input:
        list_len -= 1
        # put the number in the correct digit
        int_output += num * pow(10, list_len)
    print(int_output)


list_input = [8, 3, 5, 1]
list_to_int(list_input)
