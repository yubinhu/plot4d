# Plot 4D package

This is a simple package for plotting arbitrary 4D functions.

There seems to be no current python library available for visualizing arbitrary 4-dimensional functions, so here's one :)

Function w(x, y, z) is visualized as a gif where each frame is a cross-section at w(x, y, z=z_plot), and the fourth dimension (value of w) is represented by color.

Example result:
![Alt Text](https://github.com/yubinhu/plot4d/blob/main/tests/example.gif)

## Install

- Via [PyPI](https://pypi.org/project/plot4d/)

  ```sh
  pip install plot4d
  ```

## Functions

- `plotter.plot4d_CS` for plotting a single cross-section for an arbitrary 4D function
- `plotter.plot4d` for generating a series of cross-section plots for an arbitrary 4D function

## Quick Start
Basic use examples can be found here: [basic tour notebook](https://github.com/yubinhu/plot4d/blob/main/tests/example.ipynb).
