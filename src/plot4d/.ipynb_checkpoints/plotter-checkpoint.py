import os
from typing import Optional
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=200
import numpy as np
import imageio
from dataclasses import dataclass

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
    
def _evaluate(func, frame:Frame2D, z):
    x = np.linspace(frame.xmin, frame.xmax, frame.xnum)
    y = np.linspace(frame.ymin, frame.ymax, frame.ynum)
    w = np.array([func(i,j,z) for j in y for i in x])
    return x, y, w

def _plot(x, y, w, frame, z_plot, z_label, wbounds=None, color_num=21, path=None, func_name=None, show=True):
    # Save plot if path is set, show plot if show==True. Otherwise do nothing and return nothing. 
    X, Y = np.meshgrid(x, y)
    W = w.reshape(frame.xnum, frame.ynum)
    
    if wbounds == None:
        wbounds = (W.min(), W.max())
    wmin, wmax = wbounds
    levels = np.linspace(wmin, wmax, color_num)
    img=plt.contourf(X, Y, W, levels=levels)
    plt.colorbar(img)
    
    plt.xlabel(frame.xlabel)
    plt.ylabel(frame.ylabel)
    if func_name == None:
        func_name = "Crosssection"
    title_str = "%s at %s=%.2f"%(func_name, z_label, z_plot)
    plt.title(title_str)
    
    filename = None
    if path:
        save_path = path
        save_path += '/' if path[-1]!= '/' else ''
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    
        filename = save_path + title_str + ".png"
        plt.savefig(filename)
        
    plt.show() if show else plt.close()
    
    return filename

def plot4d_CS(func, z_plot, z_label='z', frame=Frame2D(), wbounds=None, color_num=21, path=None, func_name=None):
    """Plot a 4D function w(x,y,z) at z=z_plot with a countour plot.

    Args:
        func: function to plot
        bound2d: Class Bound2d object.
        wbounds: bounds on the w axis (color dimension). If not provided with be auto fitted.
        color_num: Number of colors to be used for countour plot. Defaults to 21.
        path: Path to save the generated plot. If None image is not saved. 
        func_name: Name to be displayed in the title of the plot

    Returns:
        None
    """
    x, y, w = _evaluate(func, frame, z_plot)
    _plot(x, y, w, frame, z_plot, z_label, wbounds, color_num, path, func_name)

def plot4d(func, z_values, path="", wbounds=None, frame=Frame2D(), save_images=False, color_num = 21, fps=1, func_name=None, z_label='z', png_path=None):
    """Plot a 4D function w(x,y,z) by crosssections and create a gif for it. 

    Args:
        func (function): Function to plot.
        z_values (interable): Values of z at cross sections we want to plot at.
        png_path (str, optional): Path for generated images. Default to None. 
        wbounds (tuple, optional): Color bar range. If None then auto set. 
        bound2d (Bound2d, optional): Bounds on x and y. Default to (xmin=0, xmax=1, ymin=0, ymax=1). 
        func_name (str, optional): Name of the 4D function we are plotting. 
        z_label (str, optional): Label on the z axis. Defaults to 'z'.
        save_images (bool, optional): If true then save the cross section png files. Defaults to True.
        fps (int, optional): Frames per second used in gif. Defaults to 1.

    Returns:
        gif_name: name of gif generated in the same folder
    """    
    if png_path==None:
        png_path = os.getcwd() + "/plot4d_temp"
    filenames = []
    
    values = []
    
    if not wbounds:
        # find the wbounds first then plot
        wmin = +float('inf')
        wmax = -float('inf')
        for z in z_values:
            x, y, w = _evaluate(func, frame, z)
            wmin = min(wmin, w.min())
            wmax = max(wmax, w.max())
            values.append((x,y,w,z))
        
        for x,y,w,z in values:
            fn = _plot(x, y, w, frame, z, z_label, (wmin, wmax), color_num, png_path, func_name, show=False)
            filenames.append(fn)
    else:
        for z in z_values:
            x, y, w = _evaluate(func, frame, z)
            fn = _plot(x, y, w, frame, z, z_label, (wmin, wmax), color_num, png_path, func_name, show=False)
            filenames.append(fn)
    
    gif_name = "Cross Sections" if func_name==None else func_name
    gif_name += ".gif"
    gif_name = path+gif_name
    with imageio.get_writer(gif_name, mode='I', fps=fps) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            if not save_images:
                os.remove(filename)

    # remove path if folder is empty
    if not os.listdir(png_path):
        os.rmdir(png_path)
        
    print("Animation saved as \"%s\""%gif_name)
    
    return gif_name

@dataclass
class Frame3D: 
    xmin: Optional[float] = None
    xmax: Optional[float] = None
    ymin: Optional[float] = None
    ymax: Optional[float] = None
    zmin: Optional[float] = None
    zmax: Optional[float] = None
    xlabel: str = "x"
    ylabel: str = "y"
    zlabel: str = "z"
    
def plot4d_data(X: np.ndarray, y: np.ndarray, frame=Frame3D(), best_highlight=False, title="test", c_label="", save=False):
    """Plot 4 Dimensional Data. Optionally saves to "{title}.png"

    Args:
        X (np.ndarray): Data matrix. Shape (N, 3), where N is the number of data points
        y (np.ndarray): Label matrix. Shape (N, )
        frame (Frame3D, optional): 3D frame of the plot. Any limit not set in frame will be auto fitted. 
        best_highlight (bool, optional): Highlight the point with largest y value. Defaults to False.
        title (str, optional): Title of the plot. Defaults to "test".
        c_label (str, optional): Colorbar label. Defaults to empty string.
        save (bool, optional): Choose to save image. Defaults to False. 
    """
    assert X.shape[0] == y.shape[0]
    
    if len(y.shape) > 1:
            # TODO: plot points with different sizes as the 5th dimension
            raise NotImplementedError()
    
    xpts, ypts, zpts, sizepts, magpts = list(X[:,0]), list(X[:,1]), list(X[:,2]), list(np.zeros_like(X[:,0])), list(y)
    
    # plotting
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    
    xr, yr, zr, sr, mr = xpts[:],  ypts[:],  zpts[:], sizepts[:], magpts[:]
    if best_highlight:
        # seperate the best from the rest
        bi = np.argmax(magpts) # best index
        xb, yb, zb, sb, mb = xr.pop(bi),  yr.pop(bi),  zr.pop(bi), sr.pop(bi), mr.pop(bi)

    graph = ax.scatter(xr, yr, zr,
            c=mr, vmin=min(magpts),vmax=max(magpts), linewidths=0.5, alpha=.7)
    if best_highlight:
        ax.scatter(xb, yb, zb, 
                c=mb, vmin=min(magpts),vmax=max(magpts), edgecolor='red', linewidths=0.5, alpha=.7)

    cbar = fig.colorbar(graph)
    cbar.set_label(c_label)
    ax.set_xlabel(frame.xlabel)
    ax.set_ylabel(frame.ylabel)
    ax.set_zlabel(frame.zlabel)

    if frame.xmin and frame.xmax: ax.set_xlim([frame.xmin,frame.xmax])
    if frame.ymin and frame.ymax: ax.set_ylim([frame.ymin,frame.ymax])
    if frame.zmin and frame.zmax: ax.set_zlim([frame.zmin,frame.zmax]) #TODO: (wishlist) enable user to set max and min seperately

    plt.title(title)
    if save: plt.savefig(title+".png")
    plt.show()