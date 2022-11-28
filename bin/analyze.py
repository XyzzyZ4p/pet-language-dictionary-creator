#!/usr/bin/env python3
import sys
import pickle
from tqdm import tqdm
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from src import *


def main():
    result_list = Counter()

    for book in BOOKS:
        with open(book) as fp:
            text = fp.read()

        words = convert(text)
        frequency_list = get_frequency_list_from_words(words)
        result_list += frequency_list

    dictionary = []
    for word, quantity in tqdm(result_list.items(), desc='Progress'):
        translation = en2ru(word)
        if translation:
            dictionary.append(dict(word=word, quantity=quantity, translation=translation))
        else:
            result_list[word] = 0

    total = result_list.total()
    for obj in dictionary:
        obj['frequency'] = 100 * obj['quantity'] / total
        del obj['quantity']

    dictionary = sorted(dictionary, key=lambda x: x['frequency'], reverse=True)
    Serializer.write(SERIALIZED, dictionary)


if __name__ == '__main__':
    main()
