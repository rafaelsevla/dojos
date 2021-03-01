import string


def get_letter_value(letter):
    return string.ascii_letters.index(letter) + 1


def get_letters_sum(words):
    word_sum = 0
    for word in list(words.replace(" ", "")):
      word_sum += get_letter_value(word)
    
    return word_sum


def check_if_phrase_is_prime(phrase):
    return not get_letters_sum(phrase) % 2 == 0
