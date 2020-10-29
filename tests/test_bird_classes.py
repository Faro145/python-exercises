import pytest
from programs import bird_classes

def test_bird_owl():
    assert bird_classes.oliver.babies == 6

def test_bird_dodo():
    assert bird_classes.danny.extinct == True
