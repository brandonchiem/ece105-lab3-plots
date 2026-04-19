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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperatures against timestamps on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius. Expected shape
        is (200,).
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius. Expected shape
        is (200,).
    timestamps : numpy.ndarray
        Timestamp values in seconds corresponding to each reading. Expected
        shape is (200,).
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes to draw on.

    Returns
    -------
    None
        This function modifies ``ax`` in place and returns ``None``.
    """
    ax.scatter(timestamps, sensor_a, color="blue", label="Sensor A", alpha=0.7)
    ax.scatter(timestamps, sensor_b, color="orange", label="Sensor B", alpha=0.7)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor Readings vs Time")
    ax.legend()
    return None

# Create plot_histogram(sensor_a, sensor_b, ax) that draws the overlaid histogram
# from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid sensor temperature histograms on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius. Expected shape
        is (200,).
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius. Expected shape
        is (200,).
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes to draw on.

    Returns
    -------
    None
        This function modifies ``ax`` in place and returns ``None``.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color="blue", label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, color="orange", label="Sensor B")
    ax.axvline(
        sensor_a.mean(),
        color="blue",
        linestyle="--",
        linewidth=2,
        label="Sensor A mean",
    )
    ax.axvline(
        sensor_b.mean(),
        color="orange",
        linestyle="--",
        linewidth=2,
        label="Sensor B mean",
    )
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Count")
    ax.set_title("Temperature Distributions: Sensor A vs Sensor B")
    ax.legend()
    return None

# Create side-by-side box plot comparing Sensor A and Sensor B distributions.
# Label x-axis with sensor names, y-axis with "Temperature (deg C)".
# Add a horizontal dashed line at the overall mean of both sensors combined.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side sensor box plots on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius. Expected shape
        is (200,).
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius. Expected shape
        is (200,).
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes to draw on.

    Returns
    -------
    None
        This function modifies ``ax`` in place and returns ``None``.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(
        overall_mean,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Overall mean",
    )
    ax.set_xlabel("Sensor")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Temperature Comparison")
    ax.legend()
    return None

