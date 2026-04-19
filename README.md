# Lab 3 Sensor Plots

This project generates synthetic temperature sensor data and saves a three-panel analysis figure (scatter, histogram, and box plot).

## Installation

Activate your `ece105` Conda environment, then install dependencies:

```bash
conda activate ece105
conda install numpy matplotlib
```

If you use Mamba:

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from this directory:

```bash
python generate_plots.py
```

## Example output

The script produces one image file: `sensor_analysis.png` (150 DPI, tight bounding box). The image contains a scatter plot of Sensor A and Sensor B readings versus timestamp, an overlaid histogram of both sensor distributions with dashed mean lines, and a side-by-side box plot with a dashed overall-mean reference line.

## AI tools used and disclosure

GitHub Copilot CLI was used to help write code used in lab3_sensor_plots.ipynb and generate_plots.py. The AI assistant was given detailed prompts with the file attached to know where to make changes. The code was then reviewed and tested before being added to the file.
