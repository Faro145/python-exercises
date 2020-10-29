import pytest
from programs import decorator

def test_decorator_quiet():
    assert decorator.quiet("MORE","NOISE") == "more" + " " + "noise"