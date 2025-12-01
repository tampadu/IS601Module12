import pytest
from app.models import Calculation

def test_addition():
    calc = Calculation(a=5, b=3, type="Add")
    assert calc.compute_result() == 8

def test_division_by_zero():
    calc = Calculation(a=5, b=0, type="Divide")
    import pytest
    with pytest.raises(ValueError):
        calc.compute_result()
