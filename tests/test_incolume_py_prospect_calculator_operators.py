import pytest
from incolume.py.prospect.calculator.operators import somar, subtrair, dividir, multiplicar


# @pytest.mark.skip()
@pytest.mark.parametrize(
    ["entrance", "expected"],
    [
        (None, 0),
        ((), 0),
        ((1, 2), 3),
        ((0, 0), 0),
        ((0, 1), 1),
        ((-10, 5), -5),
        ((1.9999, .0001), 2),
        ((1,2,3,4,5,6,7,8,9), 45),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 45),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 45)
]
)
def test_somar(entrance, expected):
    assert somar(entrance) == expected

# @pytest.mark.skip()
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (None, 0),
        # ((), 0),
        ((1, 2), -1),
        ((1, 2), -1),
        ((0, 0), 0),
        ((0, 1), -1),
        ((-10, 5), -15),
        ((1.9999, .0001), 1.9998),
        (([9, 8]), 1.),
        (((9, 8)), 1.)
    ]
)
def test_subtrair(entrance, expected):
    assert subtrair(entrance) == expected



# @pytest.mark.skip()
@pytest.mark.parametrize(
    ["entrance", "expected"],
    [
        (None, 0),
        # ((), 0),
        ((1, 2), 2),
        ((0, 0), 0),
        ((0, 1), 0),
        ((-10, 5), -50),
        ((1, 1, 1, 1, 1), 1),
        ((1.9999, .0001), .00019999),
        (('1','2','3','4','5','6','7','8','9'), 362880),
        ((1., 2., 3., 4., 5., 6., 7., 8., 9.), 362880),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 362880)
]
)
def test_multiplicar(entrance, expected):
    assert pytest.approx(multiplicar(entrance), 0.000001) == expected


# @pytest.mark.skip()
@pytest.mark.parametrize(
    ["entrance", "expected"],
    [
        # (None, 0),
        # ((), 0),
        # ((0, 0), 0),
        # ((0, 0, 0, 0), 0),
        ((1, 1), 1),
        ((1, 2), .5),
        ((0, 1), 0),
        ((-10, 5), -2),
        ((1, 1, 1, 1, 1), 1),
        ((1.9999, .0001), 19999.),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.0002232142857142857),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.0002232142857142857),
        (('1','2','3','4','5','6','7','8','9'), 2.7557319223985893e-06),
]
)
def test_dividir(entrance, expected):
    assert pytest.approx(dividir(entrance)) == expected
