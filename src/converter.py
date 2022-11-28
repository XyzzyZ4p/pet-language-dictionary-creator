import re


def remove_newlines(text: str) -> str:
    text = re.sub(r'\n', ' ', text)
    return text


def text_to_word_list(text: str) -> list:
    data = text.split(' ')
    return data


def sift_empty(word_list: list) -> list:
    return list(filter(lambda x: x, word_list))


def sift_non_alpha_words(word_list: list) -> list:
    sifted_list = []
    for word in word_list:
        interrupted = False
        for character in word:
            if not character.isalpha():
                interrupted = True
                break
        if not interrupted:
            sifted_list.append(word.lower())
    return sifted_list


def convert(text: str) -> list:
    text = remove_newlines(text)
    word_list = text_to_word_list(text)
    word_list = sift_empty(word_list)
    word_list = sift_non_alpha_words(word_list)
    return word_list
