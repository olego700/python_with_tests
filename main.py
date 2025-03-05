# main.py
import requests
import numpy as np

def fetch_data(url):
    """Fetch JSON data from a given URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def compute_mean(numbers):
    """Compute the mean of a list of numbers using numpy"""
    return np.mean(numbers)

# test_main.py
import pytest
from main import fetch_data, compute_mean

def test_compute_mean():
    assert compute_mean([1, 2, 3, 4, 5]) == 3.0

def test_fetch_data(requests_mock):
    url = "https://example.com/data"
    requests_mock.get(url, json={"key": "value"})
    response = fetch_data(url)
    assert response == {"key": "value"}

