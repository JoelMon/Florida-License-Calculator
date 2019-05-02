#!/usr/bin/env python3

# Soundex constants
LETTER_TO_DROP = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
LETTER_REPLACE_1 = ['b', 'f', 'p', 'v']
LETTER_REPLACE_2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
LETTER_REPLACE_3 = ['d', 't']
LETTER_REPLACE_4 = ['l']
LETTER_REPLACE_5 = ['m', 'n']
LETTER_REPLACE_6 = ['r']


def main():
    name = input("Enter name: ")
    #   pdb.set_trace()
    print(create_soundex(name))

    return 0


def make_into_list(name):
    name = name.lower()

    return list(name)


def create_soundex(entered_name):
    initial = []
    name = make_into_list(entered_name)
    initial.append(name[0].upper())  # Append the first letter of the name to initial
    # name.pop(0)  # Remove the first letter from name before processing

    name = convert_to_number(name)
    name = remove_adjacent_letters(name)
    name = remove_first_number(name)
    name = remove_dropped_letters(name)
    name = strip_and_pad(name)
    name.insert(0, initial[0])

    name = ''.join(name)

    return name


def convert_to_number(name):
    """Replaces letters to corresponding numbers to build the soundex

    :param name:
    :type name: list
    :return: soundex
    :rtype: list

    """

    soundex = []
    for letter in name:
        if letter in LETTER_REPLACE_1:
            soundex.append('1')
        elif letter in LETTER_REPLACE_2:
            soundex.append('2')
        elif letter in LETTER_REPLACE_3:
            soundex.append('3')
        elif letter in LETTER_REPLACE_4:
            soundex.append('4')
        elif letter in LETTER_REPLACE_5:
            soundex.append('5')
        elif letter in LETTER_REPLACE_6:
            soundex.append('6')
        else:
            soundex.append(letter)

    return soundex


def remove_adjacent_letters(name):
    """

    :param name: The a name list converted to soudex numbers
    :type name: list
    :return: A list of soundex numbers with all adjacent letters with the same soundex number removed
    :rtype: list

    """

    if name == []:
        return []
    lastLetter = name[0]
    for index, element in enumerate(name[1:]):  # Starts on index 1 because lastLetter was initialized with index 0

        if element == lastLetter:
            name.pop(index)
            lastLetter = element

        elif element == 'h' or element =='w':  # If the same number is separated by 'w' or 'h' then pop the second dup.
            if name[index] == name[index+2]:
                name.pop(index)
                lastLetter = element

        else:
            lastLetter = element

    return name


def remove_first_number(name):

    name.pop(0)

    return name

def remove_dropped_letters(name):
    """Remove the vowels, y, h, and w from name

    :param name: The name to be processed
    :type name: list
    :return: name without vowels, y, h, or w
    :rtype: list

    """

    for letter in name[:]:
        if letter in LETTER_TO_DROP:
            name.remove(letter)

    return name


def strip_and_pad(name):

    if len(name) == 0:
        return ['0', '0', '0']
    elif len(name) > 3:
        name = name[:3]
    elif len(name) < 3:
        for i in range(3 - len(name)):
            name.append('0')

    return name


if __name__ == '__main__':
    main()
