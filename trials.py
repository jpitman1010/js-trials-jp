"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    # TODO: replace this line with your code
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])

    return result


def print_as_numbered_list(items):
    # TODO: replace this line with your code
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    num = start
    while num < stop:
        nums.append(num)
        num += 1
    print(nums)

def censor_vowels(word):
    vowels = ['a','e','i','o','u']
    new_word_list = []
    word.split()
    for letters in word:
        if letters in vowels:
            letters = '*'
        new_word_list.append(letters)
    return "".join(new_word_list)


def snake_to_camel(string):
    string_list = list(string)
    
    string_list[0] = string_list[0].upper()
    for i in range(len(string_list) - 1):
        if string_list[i] == '_':
            string_list[i+1] = string_list[i+1].upper()
            string_list.pop(i)
    
        
    return "".join(string_list)


def longest_word_length(words):
    longest_word = 0
    for word in words:
        word_len = len(word)
        if word_len > longest_word:
            longest_word = word_len
    return longest_word



def truncate(string):
    result = []

    string_list = list(string)
    for char in string_list:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)

def has_balanced_parens(string):
    parens = 0

    string = list(string)

    for chars in string:
        if chars == "(":
            parens += 1
        else:
            if chars == ")":
                parens -= 1
    if parens < 0:
        return False
    elif parens > 0:
        return False
    else:
        return True
        

def compress(string):
    string = list(string)
    removed_list = []
    curr_char = ''
    count = 1
    compressed = [string[0]]

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            if count >1:
                compressed.append(str(count))
            compressed.append(string[i+1])
            count = 1
    if count >1:
        compressed.append(str(count))

    print("".join(compressed))

    

        
        # if char != curr_char:
        #     curr_count += 1
        #     if curr_count > 1:
        #         compressed.append(str(curr_count))
        #     curr_char = char
        #     compressed.append(char)
        #     curr_count = 0

        # else:
        #     curr_count += 1

    # return "".join(compressed)
