def count_file_contents():
    with open('Data.txt', 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    alphabet_count = sum(char.isalpha() for line in lines for char in line)
    digit_count = sum(char.isdigit() for line in line s for char in line)

    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of alphabets: {alphabet_count}")
    print(f"Number of digits: {digit_count}")

count_file_contents()
