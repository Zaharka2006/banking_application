import pytest

from src import masks


@pytest.mark.parametrize('card_number, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('1234432156788765', '1234 43** **** 8765'),
    ('5678876543211234', '5678 87** **** 1234')
])
def test_get_mask_card_number(card_number, expected):
    assert masks.get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_card_number():
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number('123456781234567')


def test_get_mask_account_invalid_card_number():
    with pytest.raises(ValueError):
        masks.get_mask_account(123456789)


@pytest.mark.parametrize('account_number, expected', [
    ('73654108430135874305', '**4305'),
    ('73654108430135871234', '**1234'),
    ('73654108430135875678', '**5678')
])
def test_get_mask_account(account_number, expected):
    assert masks.get_mask_account(account_number) == expected


def test_get_mask_account_invalid_account_number():
    with pytest.raises(ValueError):
        masks.get_mask_account('1234567887654321')


def test_get_mask_account_invalid_type_of_account():
    with pytest.raises(ValueError):
        masks.get_mask_account(252637565846)
