import pytest
from programs import class_info

def test_test_score():
    assert class_info.John.test_score(63, 74, 82) == 73.0
