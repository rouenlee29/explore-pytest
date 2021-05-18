# taken from https://github.com/okken/talks/blob/master/2020/pycon_2020/code/test_11.py

# to run these test, run:
# python -m pytest test/
# don't just run `pytest`

import pytest
from src.triangle import triangle_type

many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid"),
]


def idfn(a_triangle):
    a, b, c, expected = a_triangle
    return f"{a}-{b}-{c}-{expected}"


@pytest.fixture(params=many_triangles, ids=idfn)
def a_triangle(request):
    return request.param


def test_fix(a_triangle):
    a, b, c, expected = a_triangle
    assert triangle_type(a, b, c) == expected
