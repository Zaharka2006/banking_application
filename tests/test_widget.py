import pytest

from src import widget


@pytest.mark.parametrize('account, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(account, expected):
    assert widget.mask_account_card(account) == expected


def test_mask_account_card_valid_account():
    with pytest.raises(TypeError):
        widget.mask_account_card(1234543221313123)


def test_mask_account_card_valid_account_name():
    with pytest.raises(ValueError):
        widget.mask_account_card('Сче 73654108430135874388')


def test_mask_account_card_valid_account_number():
    with pytest.raises(ValueError):
        widget.mask_account_card('Visa Platinum 70007922896063')


@pytest.mark.parametrize('date, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2020-05-12T02:26:18.671407', '12.05.2020'),
    ('2022-13-05T02:26:18.671407', '05.13.2022')
])
def test_get_date(date, expected):
    assert widget.get_date(date) == expected


@pytest.mark.parametrize('date', [
    '2024/03/11T02:26:18.671407',
    '1234567812345678'
    'asdfghjkasdfghjk'
    ''
])
def test_get_date_invalid_date(date):
    with pytest.raises(ValueError):
        widget.get_date(date)


@pytest.mark.parametrize('date', [
    '2024/03/11T02:26:18.671407',
    '2024.03-11T02:26:18.671407',
    '2024-03/11T02:26:18.671407',
])
def test_get_date_invalid_dash(date):
    with pytest.raises(ValueError):
        widget.get_date(date)
