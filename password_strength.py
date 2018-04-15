from string import punctuation
import re
import sys
import getpass


def load_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_blacklisted_list(loaded_file):
    return loaded_file.split()


def has_appropriate_len(password):
    return True if len(password) > 7 else False


def has_numbers(password):
    return any(letter.isdigit() for letter in password)


def has_upper(password):
    return any(letter.isupper() for letter in password)


def has_lower(password):
    return any(letter.islower() for letter in password)


def has_special_char(password):
    return any(letter in punctuation for letter in password)


def hasnt_blacklisted_words(password, blacklisted_words):
    if not blacklisted_words:
        return False
    blacklisted_words = blacklisted_words
    return bool(password.lower() not in blacklisted_words)


def hasnt_date(password):
    date_pattern = re.search('\d{6,}', password)
    return not bool(date_pattern)


def get_password_strength(password, blacklisted_words):
    extra_point = 2
    score = 0
    score = sum(((has_appropriate_len(password) * extra_point),
                has_numbers(password), (has_upper(password) * extra_point),
                has_lower(password),
                (has_special_char(password) * extra_point),
                hasnt_blacklisted_words(password, blacklisted_words),
                hasnt_date(password)))
    return score


if __name__ == '__main__':
    if len(sys.argv) != 2:
        blacklisted_words_list = None
        print('Проверка по blacklist-справочнику проводиться не будет!')
    else:
        filepath = sys.argv[1]
        try:
            blacklisted_words_data = load_file(filepath)
        except FileNotFoundError:
            sys.exit('Указан неправильный путь к файлу!')
        blacklisted_words_list = get_blacklisted_list(blacklisted_words_data)
    password = getpass.getpass()
    score = get_password_strength(password, blacklisted_words_list)
    print('Оценка вашего пароля: {}!'.format(score))
