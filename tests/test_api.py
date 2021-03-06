""" These test make sure the JService API is working as I expect. """

from api_calls import jservice_api


def test_random_question_api_status():
    random_clue = jservice_api.random_clue()[0]
    # If an error occurs None will be returned.
    # Use pytest with the [-s] flag to print the errors in the console.
    assert random_clue


def test_random_question_api_shape():
    # Making sure the shape of the API didn't change.
    random_clue = jservice_api.random_clue()[0]
    expected_keys = ['id', 'answer', 'question', 'value', 'airdate', 'created_at', 'updated_at', 'category_id',
                     'game_id', 'invalid_count', 'category']
    returned_keys = [key for key in random_clue.keys()]
    assert returned_keys == expected_keys


def test_random_question_return_multiple_questions():
    # Test that the count param is working as expected..
    random_clue = jservice_api.random_clue(count=10)
    assert len(random_clue) == 10


def test_clue_api():
    clue = jservice_api.clue()[0]
    # If an error occurs None will be returned.
    # Use pytest with the [-s] flag to print the errors in the console.
    assert clue


def test_clue_api_shape():
    # Making sure the shape of the API didn't change.
    clue = jservice_api.clue()[0]
    expected_keys = ['id', 'answer', 'question', 'value', 'airdate', 'created_at', 'updated_at', 'category_id',
                     'game_id', 'invalid_count', 'category']
    returned_keys = [key for key in clue.keys()]
    assert returned_keys == expected_keys


def test_clue_params():
    clues = jservice_api.clue(value=800, category=1)
    for clue in clues:
        assert clue['value'] == 800
        assert clue['category_id'] == 1


def test_clue_pagination():
    clues = []
    offset = 0
    for i in range(4):
        clues += jservice_api.clue(offset=offset)
        offset += 100
    assert len(clues) == 400  # Each page is 100


def test_categories_api():
    categories = jservice_api.categories()
    # If an error occurs None will be returned.
    # Use pytest with the [-s] flag to print the errors in the console.
    assert len(categories) == 100
    assert categories


def test_categories_api_shape():
    # Making sure the shape of the API didn't change.
    categories = jservice_api.categories()[0]
    expected_keys = ['id', 'title', 'clues_count']
    returned_keys = [key for key in categories.keys()]
    assert returned_keys == expected_keys


def test_categories_pagination():
    clues = []
    offset = 0
    for i in range(4):
        clues += jservice_api.categories(offset=offset)
        offset += 100
    assert len(clues) == 400  # Each page is 100
