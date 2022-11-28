#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from src import *


def main():
    data = Serializer.read(SERIALIZED)
    data = sorted(data, key=lambda x: x['frequency'], reverse=True)
    headers = data[0].keys()
    Table.write(DICTIONARY, headers=headers, data=data)


if __name__ == '__main__':
    main()
