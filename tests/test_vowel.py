import pytest
from programs import vowels

def test_vowels_onomatopoeia():
    assert vowels.vowels('Onomatopoeia') == 8
