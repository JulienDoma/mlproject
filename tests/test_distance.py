# tests/test_distance.py
from mlproject.distance import haversine

def test_type_returned():
    assert type(haversine(30,30,30,30)) == float