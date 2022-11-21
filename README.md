# Plot4D Package

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
- `plotter.plot4d` for generating an animation of cross-section plots for an arbitrary 4D function

Inputs and returns are well documented in the docstrings.

## Quick Start

Basic use examples can be found here: [basic tour notebook](https://github.com/yubinhu/plot4d/blob/main/tests/example.ipynb).

## Notes

Input parameter "frame" should be an instance of plotter.Frame2D as defined here:

```python
@dataclass
class Frame2D: 
    xmin: float = 0
    xmax: float = 1
    ymin: float = 0
    ymax: float = 1
    xlabel: str = "x"
    ylabel: str = "y"
    xnum: int = 20 # number of sample points in the x direction
    ynum: int = 20 # number of sample points in the y direction
```