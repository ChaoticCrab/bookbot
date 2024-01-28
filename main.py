with open("/home/server/workspace/github.com/ChaoticCrab/bookbot/Frankenstein.txt") as f:
    file_contents = f.read()

def word_count(string):
    word_list = string.split()
    return len(word_list)

def letter_count(string):
    letters = {}
    text = string.lower()
    for elem in text:
        if elem not in letters:
            letters[elem] = 1
        else:
            letters[elem] += 1
    return letters

def print_report(dict):
    print(dict)
    for char, count in dict.items():
        if char.isalpha():
            print("The " + str(char) + " character was found " + str(count) + " times")
    
print_report(letter_count(file_contents))
