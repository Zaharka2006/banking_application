import pytest

from src import processing


@pytest.mark.parametrize('state, expected', [
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])
])
def test_filter_by_state(operations_list, state, expected):
    assert processing.filter_by_state(operations_list, state) == expected


def test_filter_by_state_valid_status(operations_list):
    with pytest.raises(ValueError):
        processing.filter_by_state(operations_list, 'afgag')


@pytest.mark.parametrize('is_reverse, expected', [
    (True, [
        {'date': '2019-07-03T18:35:29.512364',
         'id': 41428829,
         'state': 'EXECUTED'
         },
        {'date': '2018-10-14T08:21:33.419441',
         'id': 615064591,
         'state': 'CANCELED'
         },
        {'date': '2018-09-12T21:27:25.241689',
         'id': 594226727,
         'state': 'CANCELED'
         },
        {'date': '2018-06-30T02:08:58.425572',
         'id': 939719570,
         'state': 'EXECUTED'
         }
    ]),
    (False, [
        {'date': '2018-06-30T02:08:58.425572',
         'id': 939719570,
         'state': 'EXECUTED'},
        {'date': '2018-09-12T21:27:25.241689',
         'id': 594226727,
         'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441',
         'id': 615064591,
         'state': 'CANCELED'},
        {'date': '2019-07-03T18:35:29.512364',
         'id': 41428829,
         'state': 'EXECUTED'}
    ])
])
def test_sort_by_date(operations_list, is_reverse, expected):
    assert processing.sort_by_date(operations_list, is_reverse) == expected


def test_sort_by_date_valid_format():
    with pytest.raises(ValueError):
        processing.sort_by_date([
            {'date': '2018-06-30T02:08:58.425572',
             'id': 939719570,
             'state': 'EXECUTED'},
            {'date': '2018-16-12T21:27:25.241689',
             'id': 594226727,
             'state': 'CANCELED'},
            {'date': '2018-10-14T08:21:33.419441',
             'id': 615064591,
             'state': 'CANCELED'},
            {'date': '2019-20-03T18:35:29.512364',
             'id': 41428829,
             'state': 'EXECUTED'}
        ])


# def test_sort_by_date_valid_unique_date(operations_list):
