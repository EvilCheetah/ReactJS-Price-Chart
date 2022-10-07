import json
from os import getenv
from pathlib import Path


def save_data(data: list[dict]) -> None:
    with open( 
        file = Path(getenv('OUTPUT_DIRECTORY')) / Path(getenv('OUTPUT_FILENAME')),
        mode = 'w'
    ) as fout:
        json.dump(data, fout)