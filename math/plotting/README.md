# Plotting

A project on data visualization with `matplotlib` in Python 3.

## Description

This project covers the fundamentals of plotting data using
`matplotlib.pyplot`. It includes line graphs, scatter plots,
histograms, bar graphs, stacked bar graphs, axis scaling
(including logarithmic), labeling, legends, and combining
multiple plots into a single figure with `subplot2grid`.

## Requirements

- Ubuntu 16.04 LTS
- Python 3.5
- numpy 1.15
- matplotlib 3.0
- pycodestyle 2.5
- All files start with `#!/usr/bin/env python3`, end with a
  newline, are executable, and are documented (module,
  class, and function docstrings).

## Files

| File | Description |
| --- | --- |
| `0-line.py` | Plots `y = x^3` as a solid red line, x-axis from 0 to 10. |
| `1-scatter.py` | Scatter plot of men's height vs. weight in magenta. |
| `2-change_scale.py` | Line graph of C-14 exponential decay with a logarithmic y-axis. |
| `3-two.py` | Two line graphs (C-14 and Ra-226 decay) on one set of axes, with a legend. |
| `4-frequency.py` | Histogram of student grades, binned every 10 units. |
| `5-all_in_one.py` | Combines the five plots above into one 3x2 figure. |
| `6-bars.py` | Stacked bar graph of fruit quantities per person. |

## Usage

Each script can be run directly, e.g.:

```
./0-line.py
```

This will display the corresponding plot in a window (requires
a working X11/GUI backend).

## Author

ALU Machine Learning Foundations - Plotting project.
