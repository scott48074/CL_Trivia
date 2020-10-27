#!/usr/bin/env python3
""" The API callers to get the questions. See http://jservice.io/ for more information on the APi. """
from typing import List, Dict, Union

from requests.exceptions import HTTPError
import requests
import json


# Type hints: returning a list of dictionaries or None in case of an error.
def random_question(count: int = 1) -> Union[List[Dict[str, str]], None]:
    # Count is the number of questions to return (100 max).
    try:
        params = {'count': str(count)}
        r = requests.get('http://jservice.io/api/random', params=params)
        r.raise_for_status()
        return json.loads(r.text)
    except HTTPError as e:
        print(f'HTTP error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def main():
    pass


if __name__ == '__main__':
    main()
