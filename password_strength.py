from string import punctuation
import re
import sys


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


def hasnt_blacklisted_words(password):
    blacklist = ['password', 'mail', 'cat', 'dog']
    return all(
            blacklisted_word not in password.lower()
            for blacklisted_word in blacklist
            )


def hasnt_date(password):
    date_pattern = re.search('\d{6,}', password)
    return True if not date_pattern else False


def get_password_strength(password):
    extra_point = 2
    score = 0
    score += has_appropriate_len(password) * extra_point
    score += has_numbers(password)
    score += has_upper(password) * extra_point
    score += has_lower(password)
    score += has_special_char(password) * extra_point
    score += hasnt_blacklisted_words(password)
    score += hasnt_date(password)
    return score


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Вы не ввели пароль!')
    password = sys.argv[1]
    score = get_password_strength(password)
    print('Оценка вашего пароля: {}!'.format(score))
