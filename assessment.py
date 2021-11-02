# Zweli (Zwelisha) Mthethwa

"""
Question 1.1 - Count the number of times a char appears in a string
"""


def char_appearance_count(string: str, ch: chr):
    """
    Counts the number of number of times a char appears on the given string.

    Counts the number of time the passed character appears on the passed string.

    Parameters:
    string (str): The string to check how many times the given character appears.
    ch (chr): The character to count how many times it appears on the given string

    Returns:
    int: The number of times ch appears in string
    """
    letter_count = 0
    for letter in string:
        if letter.lower() == ch.lower():
            letter_count += 1
    return letter_count


"""
Question 1.4 - Write the string “hello world” into a file where each word occupies a new line, then
read the lines out of the file and print them into stdout. Making sure to handle (at
least) the case of a non-existent or broken file.
"""


def write_to_file(file_name: str, string: str):
    """
    Writes the given string to a given file

    The string is split into words and each word is written on it's own line on the given file.

    Parameters:
    file_name (str): The name of the file to write on the string content.
    string (str): The string to write on the given file.

    Returns:
    None: Does not return a value, it is a void function.
    """
    try:
        f = open(file_name, "w")
    except FileNotFoundError:
        print("There is no such file!")
    finally:
        words = string.split(" ")
        try:
            for word in words:
                f.write(f"{word}\n")
        except IOError:
            print(
                f"There was problem with writing to {file_name} \n This file may be corrupt or have a read only permission"
            )
        finally:
            f.close()


def read_file_content(file_name: str):
    """
    Reads the content of the given file

    Prints the content of the given file to the terminal

    Parameters:
    file_name (str): The name of the file to read.

    Returns:
    None: Does not return a value, it is a void function.
    """
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        for line in lines:
            print(f"{line}\n")
        f.close()
    except FileNotFoundError:
        print(f"{file_name} file does not exist!")
    except IOError:
        print(
            f"There was problem with reading {file_name} \n This file may be corrupt or broken"
        )
    finally:
        return


"""
Question 1.5 - Sort an arbitrary array of integers in ascending order, using the Merge Sort algorithm
"""


def merge_sort_ascending(arr):
    """
    Sorts a given list of integers in ascending order.

    The sorting is done using the mnerge sort algorithm. Efficient for both small and large lists.

    Parameters:
    arr (list): A list of integers to sort

    Returns:
    None: Does not return a value, it is a void function
    """
    if len(arr) > 1:
        left_half = arr[0 : len(arr) // 2]
        right_half = arr[len(arr) // 2 :]

        # Divide ad conquer recursively
        merge_sort_ascending(left_half)
        merge_sort_ascending(right_half)

        # Merge step
        i = 0  # left  half index
        j = 0  # right right half index
        k = 0  # merged index

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Merge remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


"""
Question 2 Squares
"""

if __name__ == "__main__":
    my_list = [2, 3, 5, 10, 1, 40, 6, 0]
    print(merge_sort_ascending(my_list))
    print(my_list)
