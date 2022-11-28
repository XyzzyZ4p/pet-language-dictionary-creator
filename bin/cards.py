#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from src import *


def main():
    data = Table.read(DICTIONARY)

    headers = list(data[0].keys())
    headers.remove('frequency')

    data = list(chunk(data, 20))
    for idx, deck in enumerate(data):

        for el in deck:
            del el['frequency']

        Table.write(CARDS / f'{idx + 1}.csv', headers, deck)


if __name__ == '__main__':
    main()
