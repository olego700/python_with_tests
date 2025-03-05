
import pytest
from main import fetch_data, compute_mean

def test_compute_mean():
    assert compute_mean([1, 2, 3, 4, 5]) == 3.0

def test_fetch_data(requests_mock):
    url = "https://example.com/data"
    requests_mock.get(url, json={"key": "value"})
    response = fetch_data(url)
    assert response == {"key": "value"}
