#!/usr/bin/env python3
""" The API callers to get the questions. See http://jservice.io/ for more information on the APi. """
from typing import List, Dict, Union

import requests
from requests.exceptions import HTTPError


# Type hints: returning a list of dictionaries or None in case of an error.
def clue(**params) -> Union[List[Dict[str, str]], None]:
    """
    params:
    value(int): the value of the clue in dollars
    category(int): the id of the category you want to return
    min_date(date): earliest date to show, based on original air date
    max_date(date): latest date to show, based on original air date
    offset(int): offsets the returned clues. Useful in pagination
    """
    try:
        if params:
            params = {k: v for (k, v) in zip(params.keys(), params.items())}
        if 'offset' not in params:
            params['offset'] = 0
        r = requests.get('http://jservice.io/api/clues', params=params)
        r.raise_for_status()
        return r.json()
    except HTTPError as e:
        print(f'HTTP error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def random_clue(count: int = 1) -> Union[List[Dict[str, str]], None]:
    # Count is the number of questions to return (100 max).
    try:
        params = {'count': str(count)}
        r = requests.get('http://jservice.io/api/random', params=params)
        r.raise_for_status()
        return r.json()
    except HTTPError as e:
        print(f'HTTP error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def main():
    pass


if __name__ == '__main__':
    main()
