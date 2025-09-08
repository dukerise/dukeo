import pytest
from dukeo.services import risk

def test_calc():
    assert risk.calc_position_size(1000, 10000, 0.02) == 0.2
