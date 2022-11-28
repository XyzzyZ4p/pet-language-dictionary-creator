import os
import yaml
from pathlib import Path


ROOT = Path(__file__).parents[1]

with open(ROOT / 'conf.yaml', 'r', encoding='utf-8') as fp:
    CONF = yaml.safe_load(fp)

DATA = Path(CONF['paths']['data'].format(root=ROOT))
DICTIONARY = Path(CONF['paths']['dictionary'].format(data=DATA))
SERIALIZED = Path(CONF['paths']['serialized'].format(data=DATA))
CARDS = Path(CONF['paths']['cards'].format(data=DATA))
BOOKS = [
    file for file
    in Path(CONF['paths']['books'].format(home=os.path.expanduser('~'))).iterdir()
    if file.is_file() and 'txt' in file.suffix
]
