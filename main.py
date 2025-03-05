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


