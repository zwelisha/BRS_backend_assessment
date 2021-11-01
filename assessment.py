# Zweli (Zwelisha) Mthethwa

'''
Question 1.1 - Count the number of times a char appears in a string
'''
def char_appearance_count(string:str, ch:chr) -> int:
    letter_count = 0
    for letter in string:
        if letter == ch:
            letter_count += 1
    return letter_count

'''
Question 1.4 - writing and reading files
'''
def write_to_file(file_name:str, string:str):
    try:
        f = open(file_name, 'w')
    except FileNotFoundError:
        print('There is no such file!')
    finally:
        words = string.split(' ')
        try:
            for word in words:
                f.write(f'{word}\n')
        except IOError:
            print(f'There was problem with writing to {file_name} \n This file may be corrupt or have a read only permission')
        finally:
            f.close()

def read_file_content(file_name:str):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            print(f'{line}\n')
        f.close()
    except FileNotFoundError:
        print(f'{file_name} file does not exist!')
    except IOError:
        print(f'There was problem with reading {file_name} \n This file may be corrupt or broken')
    finally:
        return 
          

if __name__ == "__main__":
    word_string = "hello world"
    write_to_file("hello.txt",word_string) 
    read_file_content("hello.txt")   