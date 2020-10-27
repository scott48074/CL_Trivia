""" These test make sure the JService API is working as I expect. """

from api_calls import jservice_api


def test_random_question_api_status():
    random_questions = jservice_api.random_question()[0]
    # If an error occurs None will be returned.
    # Use pytest with the [-s] flag to print the errors in the console.
    assert random_questions


def test_random_question_api_shape():
    # Making sure the shape of the API didn't change.
    random_questions = jservice_api.random_question()[0]
    expected_keys = ['id', 'answer', 'question', 'value', 'airdate', 'created_at', 'updated_at', 'category_id',
                     'game_id', 'invalid_count', 'category']
    returned_keys = [key for key in random_questions.keys()]
    assert returned_keys == expected_keys


def test_random_question_return_multiple_questions():
    # Test that the count param is working as expected..
    random_questions = jservice_api.random_question(count=10)
    assert len(random_questions) == 10
