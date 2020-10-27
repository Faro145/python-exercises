import pytest
import list_of_squares

def test_listofsquares_six():
    assert list_of_squares.list_of_squares(6) == {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}