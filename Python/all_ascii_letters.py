
import string


def all_letter(input):
    all_letters_englisc = string.ascii_letters
    for i in range(len(input)):
        if input[i] not in all_letters_englisc:
            return False

    return True


input_string = input("Please enter a string: ")
print(all_letter(input_string))