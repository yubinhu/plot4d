# Plot4D Package

This is a package for **plotting arbitrary 4D functions**.

Function w(x, y, z) is visualized as an animation where each frame is a 2D cross-section w(x, y, z=z_plot) with the fourth dimension represented by color.

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
