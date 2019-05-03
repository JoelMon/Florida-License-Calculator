#!/usr/bin/python3

"""
Calculates driver licenses for the state of Florida.
"""

import soundex


def main():
    """Main function that runs the program

    This function asks the user for the needed information to be able to
    calculate a driver license ID.

    :return: True if the function ends successfully
    :rtype: bool
    """
    first_name = input("First name: ")
    last_name = input('Last name: ')
    middle_name = input('Middle initial: ')
    birth_year = input('Birth year: ')
    birth_month = input('Birth month : ')
    birth_day = input('Birth day: ')
    sex = input('Sex (M for Male | F for Female: ')

    first_name_encoded = encode_first_name(first_name,
                                           middle_name
                                           )
    last_name_encoded = soundex.create_soundex(last_name)
    birth_year_encoded = encode_birth_year(birth_year)
    birth_month_day_encoded = encode_month_day(birth_month,
                                               birth_day, sex
                                               )

    print("\nLic #: %s-%s-%s-%s-0" % (last_name_encoded,
                                      first_name_encoded,
                                      birth_year_encoded,
                                      birth_month_day_encoded
                                      ))

    return True


def encode_first_name(name, middle_name):
    """Encodes name and/or middle name

    :param name: The first name to encode
    :param middle_name: The middle name to encode
    :return: The name(s) encoded

    """
    name = name.lower()
    middle_name = middle_name.lower()

    name_table = {'albert'   : 20, 'alice': 20, 'ann': 40, 'anna': 40,
                  'anne'     : 40, 'annie': 40, 'arthur': 40, 'bernard': 80,
                  'bette'    : 80, 'bettie': 80, 'betty': 80, 'carl': 120,
                  'catherine': 120, 'charles': 120, 'dorthy': 180,
                  'edward'   : 220, 'elizabeth': 220, 'florence': 260,
                  'donald'   : 180, 'clara': 140, 'frank': 260, 'george': 300,
                  'grace'    : 300, 'harold': 340, 'harriet': 340,
                  'harry'    : 360, 'hazel': 360, 'helen': 380, 'henry': 380,
                  'james'    : 440, 'jane': 440, 'jayne': 440, 'jean': 460,
                  'joan'     : 480, 'john': 460, 'joseph': 480,
                  'margaret' : 560, 'martin': 560, 'marvin': 580, 'mary': 580,
                  'melvin'   : 600, 'mildred': 600, 'patricia': 680,
                  'paul'     : 680, 'richard': 740, 'robert': 760, 'ruby': 740,
                  'ruth'     : 760, 'thelma': 820, 'thomas': 820,
                  'walter'   : 900, 'wanda': 900, 'william': 920, 'wilma': 920}

    name_initial_table = {'a': 0, 'b': 60, 'c': 100, 'd': 160, 'e': 200,
                          'f': 240, 'g': 280, 'h': 320, 'i': 400, 'j': 420,
                          'k': 500, 'l': 520, 'm': 540, 'n': 620, 'o': 640,
                          'p': 660, 'q': 700, 'r': 720, 's': 780, 't': 800,
                          'u': 840, 'v': 860, 'w': 880, 'x': 940, 'y': 960,
                          'z': 980}

    middle_name_initial_table = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                                 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                                 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 14,
                                 'p': 15, 'q': 15, 'r': 16, 's': 17, 't': 18,
                                 'u': 18, 'v': 18, 'w': 19, 'x': 19, 'y': 19,
                                 'z': 19}

    if name in name_table:
        if middle_name == '':
            name_encoded = name_table[name]
            return '{:03d}'.format(name_encoded)
        else:
            name_encoded = name_table[name] + \
                           middle_name_initial_table[middle_name[0]]
            return '{:03d}'.format(name_encoded)
    elif middle_name == '':
        name_encoded = name_initial_table[name[0]]
        return '{:03d}'.format(name_encoded)
    else:
        name_encoded = name_initial_table[name[0]] + \
                       middle_name_initial_table[middle_name[0]]
        return '{:03d}'.format(name_encoded)


def encode_birth_year(birth_year):
    """Returns the last two digits of the birth year entered

    :param birth_year: The birth year in 19xx format
    :return: The last two digits of the birth year

    """
    return birth_year[-2:]


def encode_month_day(month, day, sex):
    """Encode birth month, day, and sex

    :param month: Birth month to be encoded
    :type month: str
    :param day: Birth day to be encoded
    :type day: str
    :param sex: Sex to be encoded
    :type sex: str
    :return: The encoding of Birth month, day, and sex
    :rtype: int

    """
    sex.lower()
    month = int(month)
    day = int(day)

    if sex == 'm':
        return (month - 1) * 40 + day
    else:
        return (month - 1) * 40 + day + 500


if __name__ == '__main__':
    main()
