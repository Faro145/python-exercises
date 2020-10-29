import pytest
from programs import route_planner

def test_route_list():
    assert route_planner.route_planner([1,3,5,7,9,2,4,6,8,10]) == [1,3,5,2,4,6]
