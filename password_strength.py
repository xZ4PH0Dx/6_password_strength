from string import punctuation
import re
import sys
import getpass


def load_blacklist(filepath):
    with open(filepath, 'r') as file:
        loaded_blacklist = file.read()
    return loaded_blacklist.splitlines()


def has_appropriate_len(password):
    good_passwd_len = 7
    return True if len(password) > good_passwd_len else False


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
    return password.lower() not in blacklisted_words


def hasnt_date(password):
    date_pattern = re.search('\d{6,}', password)
    return not bool(date_pattern)


def get_password_strength(password, blacklisted_words):
    extra_point = 2
    score = 0
    score = sum((
        has_appropriate_len(password) * extra_point,
        has_numbers(password),
        has_upper(password) * extra_point,
        has_lower(password),
        has_special_char(password) * extra_point,
        hasnt_blacklisted_words(password, blacklisted_words),
        hasnt_date(password))
    )
    return score


if __name__ == '__main__':
    if len(sys.argv) != 2:
        blacklisted_words_data = None
        print('Проверка по blacklist-справочнику проводиться не будет!')
    else:
        filepath = sys.argv[1]
        try:
            blacklisted_words_data = load_blacklist(filepath)
        except FileNotFoundError:
            sys.exit('Указан неправильный путь к файлу!')
    password = getpass.getpass()
    score = get_password_strength(password, blacklisted_words_data)
    print('Оценка вашего пароля: {}!'.format(score))
