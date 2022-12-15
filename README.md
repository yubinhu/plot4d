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

## Quick Start

- `plotter.plot4d_CS(f, z_plot)` plots a single cross-section of $f(x, y, z)$ at $z_{plot}$.

  Example use: `plotter.plot4d_CS(lambda x, y, z: x+y+z, 10)`

- `plotter.plot4d(f, z_values)` generates an animation of cross-section plots at $z \in z_{values}$ for $f(x, y, z)$ (See example result above).

  Example use: `plotter.plot4d(lambda x, y, z: x**2+y-y**3*z, range(0,5))`

- `plotter.plot4d_data(X, y)` helps visualize your data. X has shape $n \times d$ and y has shape $n \times 1$.

More examples can be found here: [basic tour notebook](https://github.com/yubinhu/plot4d/blob/main/tests/example.ipynb).

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
