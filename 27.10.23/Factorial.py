There is a file name 'Data.txt' which stores some data. write a program taht reads the contents of that file and count how many lines words, alphabets and digits are there in this file 

def count_statistics(text):
    lines = len(text.split('\n'))
    words = sum(len(line.split()) for line in text.split('\n'))
    alphabets = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)

    return lines, words, alphabets, digits

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

if __name__ == "__main__":
    file_path = 'Data.txt'
    file_content = read_file(file_path)

    if file_content is not None:
        lines, words, alphabets, digits = count_statistics(file_content)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of alphabets: {alphabets}")
        print(f"Number of digits: {digits}")



There is a file name 'Data.txt' which stores some data. write a program taht reads the contents of that file and count how many lines words, alphabets and digits are there in this file 
def count_file_contents():
    with open('Data.txt', 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    alphabet_count = sum(char.isalpha() for line in lines for char in line)
    digit_count = sum(char.isdigit() for line in lines for char in line)

    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of alphabets: {alphabet_count}")
    print(f"Number of digits: {digit_count}")

count_file_contents()