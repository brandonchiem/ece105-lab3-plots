"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.


def generate_data(seed):
    """Generate synthetic sensor temperature readings and timestamps.

    Parameters
    ----------
    seed : int
        Seed for initializing NumPy's random generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius with shape (200,),
        sampled from a normal distribution with mean 25 and standard
        deviation 3.
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius with shape (200,),
        sampled from a normal distribution with mean 27 and standard
        deviation 4.5.
    timestamps : numpy.ndarray
        Timestamp values in seconds with shape (200,), sampled uniformly
        from 0 to 10.
    """
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)
    timestamps = rng.uniform(low=0, high=10, size=200)
    return sensor_a, sensor_b, timestamps
