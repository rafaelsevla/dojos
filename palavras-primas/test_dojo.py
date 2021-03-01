from main import get_letter_value, get_letters_sum, check_if_phrase_is_prime


def test_a_should_return_1():
    assert get_letter_value('a') == 1


def test_b_should_return_2():
    assert get_letter_value('b') == 2


def test_A_should_return_27():
    assert get_letter_value('A') == 27


def test_Z_should_return_52():
    assert get_letter_value('Z') == 52


def test_should_return_3():
    assert get_letters_sum('aaa') == 3


def test_should_return_4():
    assert get_letters_sum('bb') == 4


def test_should_return_4():
    assert get_letters_sum('c b a') == 6


def test_should_return_false():
    assert check_if_phrase_is_prime('bb') == False


def test_should_return_true():
    assert check_if_phrase_is_prime('bba') == True