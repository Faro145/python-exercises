import pytest
from programs import factorial

def test_fact_zero():
    assert factorial.fact(0) == 1
