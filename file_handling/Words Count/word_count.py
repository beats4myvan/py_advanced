import re


def write_result(res):
    with open('output.txt', 'w') as file:
        for r in res:
            file.writelines(r+"\n")


def get_file_words(path_to_file):
    with open(path_to_file, 'r') as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-zA-Z']+", text.lower())
        # return [line.split() for line in file.readlines()]


path_to_words = "words.txt"
path_to_text = "text.txt"

analyse = {}

first_words = get_file_words(path_to_words)
second_file_words = get_file_words(path_to_text)

for word in first_words:
    if word in second_file_words:
        analyse[word] = second_file_words.count(word)

result = [f"{el[0]} - {el[1]}" for el in sorted(analyse.items(), key=lambda x: -x[1])]
write_result(result)