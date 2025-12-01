import pytest
from app.models import Calculation

def test_compute_add():
    c = Calculation(a=2, b=3, type="Add")
    assert c.compute_result() == 5

def test_compute_sub():
    c = Calculation(a=5, b=2, type="Sub")
    assert c.compute_result() == 3

def test_compute_multiply():
    c = Calculation(a=4, b=3, type="Multiply")
    assert c.compute_result() == 12

def test_divide_by_zero_raises():
    c = Calculation(a=5, b=0, type="Divide")
    with pytest.raises(ValueError):
        c.compute_result()
