import pickle
import csv
from pathlib import Path
from typing import Any, Dict, List


class Serializer:
    @classmethod
    def write(cls, file: Path, data: Any) -> None:
        with open(file, 'wb') as fp:
            pickle.dump(data, fp)

    @classmethod
    def read(cls, file: Path) -> Any:
        with open(file, 'rb') as fp:
            data = pickle.load(fp)
        return data


class Table:
    @classmethod
    def write(cls, path: Path, headers: list, data: List[Dict]) -> None:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=headers,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()

            for obj in data:
                writer.writerow(obj)

    @classmethod
    def read(cls, path: Path) -> Any:
        data = []
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
