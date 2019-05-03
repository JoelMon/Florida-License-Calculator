import pytest
import main


@pytest.mark.parametrize('name, middle_name, expected', [
                        ('albert', '', '020'),
                        ('donald', '', '180'),
                        ('wanda', '', '900')
                        ])
def test_encode_first_name(name, middle_name, expected):
    result = main.encode_first_name(name, middle_name)
    assert result == expected


@pytest.mark.parametrize('name, middle_name, expected', [
                        ('albert', 'angle', '021'),
                        ('donald', 'tom', '198'),
                        ('wanda', 'queen', '915')
                        ])
def test_encode_first_name_with_middle_name(name, middle_name, expected):
    result = main.encode_first_name(name, middle_name)
    assert result == expected


@pytest.mark.parametrize('name, middle_name, expected', [
                        ('joel', '', '420'),
                        ('manolo', '', '540'),
                        ('vivi', '', '860')
                        ])
def test_encode_first_name_not_in_table(name, middle_name, expected):
    result = main.encode_first_name(name, middle_name)
    assert result == expected


@pytest.mark.parametrize('name, middle_name, expected', [
                        ('joel', 'wats', '439'),
                        ('manolo', 'cuba', '543'),
                        ('vivi', 'rosa', '876')
                        ])
def test_encode_first_name_not_in_table_middle(name, middle_name, expected):

    result = main.encode_first_name(name, middle_name)
    assert result == expected


@pytest.mark.parametrize('name, middle_name, expected', [
                        ('joel', 'wats', '439'),
                        ('manolo', 'cuba', '543'),
                        ('vivi', 'rosa', '876')
                        ])
def test_encode_first_name_not_in_table_middle(name, middle_name, expected):
    result = main.encode_first_name(name, middle_name)
    assert result == expected


@pytest.mark.parametrize('birth_year, expected', [
                        ('1990', '90'),
                        ('1980', '80'),
                        ('1959', '59')
                        ])
def test_encode_birth_year(birth_year, expected):

    result = main.encode_birth_year(birth_year)
    assert result == expected


def test_encode_month_day(month, day, sex):
    pass
