import pytest
import soundex


def test_make_into_list_makeList():

    result = soundex.make_into_list('Robert')
    assert type(result) is list


def test_make_into_list_Lowercase():

    result = soundex.make_into_list('James')

    assert result == ['j', 'a', 'm', 'e', 's']


@pytest.mark.parametrize('list, expected', [(['j', 'a', 'm', 'e', 's'], ['j', 'm', 's']),
                                            (['j', 'o', 'l', 'e', 'e'], ['j', 'l']),
                                            (['d', 'a', 'n'], ['d', 'n']),
                                            (['w', 'a', 't', 's', 'o', 'n'], ['t', 's', 'n'])
                                            ])
def test_remove_dropped_letters(list, expected):

    result = soundex.remove_dropped_letters(list)
    assert result == expected


def test_convert_to_number():

    result = soundex.convert_to_number(['j', 'm', 's'])
    assert result == ['2', '5', '2']



@pytest.mark.parametrize('list, expected', [(['1', '2', '3', '4'], ['1', '2', '3', '4']),
                                            (['1', '2', '2', '4'], ['1', '2', '4']),
                                            (['6', '7', '6', '7', '7', '8'], ['6', '7', '6', '7', '8']),
                                            (['3', '3'], ['3']),
                                            (['2'], ['2']),
                                            ([], ['0', '0', '0'])
                                            ])
def test_remove_adjacent_letters(list, expected):

    result = soundex.remove_adjacent_letters(list)
    assert result == expected

