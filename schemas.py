from dataclasses import dataclass
from src.TimerFormat import TimerFormat
import pandas as pd

# THE SOLE INPUTS FOR PLOTTING, 
# THIS IS HOW THINGS WILL BE HANDLED
# we may want to switch the suffixes to In

###############
# Base plot dataclass
@dataclass
class Base:
    """row column for row/column placement
    in plotly subplot"""
    name : str
    row : int | None
    column : int | None 

###############
# POLAR SCATTTER PLOTS (I THINK WE ONLY NEED ONE WITH THE UPDATE)
# polar scatter base parameters
@dataclass
class ScatterpolarBase(Base):
    
    r :      list[float]
    theta :  list[str | int]
    fill :   str | None

# polar scatter parameters
@dataclass
class ScatterpolarParam(ScatterpolarBase):
    # for identifying plotgen method
    plottype : str = 'scatterpolar'
    
    # slice default values are the whole thing
    split : tuple[tuple] = ((0, -1))
    
    # spec for subplot axis layout
    spec : str = 'polar'
    rowspan : int = 1
    colspan : int = 1

    animate : bool = True


@dataclass
class ScatterPolarAxis(ScatterpolarParam):
    manual_axis : bool = False
    axis_name : bool = 'polar'

    radial_range: list[float] | None = None # this might not work
    radial_ticklables : bool = False
    radial_ticks : str = ''

    angular_ticklabels : bool = False
    angular_ticks : str | None = ''
    angular_rotation : int = 90

    x_domain : tuple[float] = (0.0, 0.5) 
    y_domain : tuple[float] = (0.0, 0.5)

@dataclass
class ScatterPolarIn(ScatterPolarAxis):
    pass

###############
# SCATTER PLOTS
@dataclass
class ScatterBase(Base):

    # xy coordinates typically a row or column
    # as pulled by loc/iloc
    x : pd.Series
    y : pd.Series

    # plotmode lines, markers, etc
    mode : str

@dataclass
class ScatterParam(ScatterBase):

    # for identifying plotgen method
    plottype: str = 'scatter'

    # slice default values are the whole thing
    split : tuple[tuple] = ((0, -1))

    # specs for subplots
    spec : str = 'xy'
    rowspan : int = 1
    colspan : int = 1

    # 
    manual_axis : bool = False
    animate : bool = False
  

@dataclass
class ScatterIn(ScatterParam):
    pass



###############
# MARKER TYPES
@dataclass
class MarkerBase:
    size : int
    color : list[float | int]
    colorscale : str
    opacity : float  = 0.8

###############
# 3D PLOTS
# scatter3d
@dataclass
class Scatter3dBase(Base):
    # xyz data
    xyz : pd.DataFrame
    
    # plotmode lines, markers, etc
    mode : str

    # 3d marker type
    marker : MarkerBase
    
    #spanning of columns/rows in subplot
    rowspan : int = 1
    colspan : int = 1

    # spec for subplot specs
    spec : str = 'scene'

     # for identifying plotgen method
    plottype: str = 'scatter3d'

    # slice default values are the whole thing
    split : tuple[tuple] = ((0, -1))

    # whether or not to be animated
    animate : bool = True


@dataclass
class Scatter3dAxis(Scatter3dBase):

    manual_axis : bool = False
    axis_name : bool = 'scene'

    xaxis_range : tuple[float|None] = (None, None)
    xaxis_nticks : int = 4

    yaxis_range : tuple[float|None] = (None, None)
    yaxis_nticks : int = 4

    zaxis_range : tuple[float|None] = (None, None)
    zaxis_nticks : int = 4

    # for placement
    x_domain : tuple[float] = (0.0, 0.5)
    y_domain : tuple[float] = (0.0, 0.5)


@dataclass
class Scatter3dIn(Scatter3dAxis):
    pass 

################
# PIE PLOTS
# Marker
@dataclass
class PieMarker:
    colors : list[str] # list of color names
    
    line_width : int = 1
    line_color : str = '#000000' 

# Base Plot 
@dataclass
class PieBase(Base):
    labels : list[str]
    values : list[int | float]
    marker : PieMarker


    textinfo : str = 'value'
    hoverinfo : str = 'label+percent'
    spec : str = 'domain'
    plottype: str = 'pie'
    manual_axis : bool = False

@dataclass
class PieIn(PieBase):
    animate : bool = False
        #spanning of columns
    rowspan : int = 1
    colspan : int = 1


###############
# 3D Surface plots
@dataclass
class SurfaceBase(Base):
    xyz: pd.DataFrame

@dataclass
class SurfaceParam(SurfaceBase):

    split : tuple[tuple] = ((0, -1))
    
    spec : str = 'scene'
    plottype : str = 'surface'

    #spanning of columns
    rowspan : int = 1
    colspan : int = 1

    animate : bool = True

    manual_axis : bool = False

@dataclass
class SurfaceIn(SurfaceParam):
    pass


###############
# FRAME PLOTS
@dataclass
class FrameBase:
    
    # a list of slices to animate over
    slices: list[list[int]]

    # list of input paramter schema
    params: list[
        ScatterPolarIn|ScatterParam|PieBase|Scatter3dBase|SurfaceIn
    ] #i think this means and/or

    # a timer for keeping track of time
    timer: TimerFormat

    # list of titles, should be in the same order as params
    subplot_titles : list[str]
    
@dataclass
class FrameParams(FrameBase):
    animate : bool = True


@dataclass
class FrameIn(FrameParams):
    pass


###############
# DATA SMOOTHER
@dataclass
class SmootherIn:
    # method (required)
    method: str

    # sub commands (all optional)
    min_periods : int | None

"""

Each item in ‘specs’ is a dictionary.
’xy’: 2D Cartesian subplot type for scatter, bar, etc.

’scene’: 3D Cartesian subplot for scatter3d, cone, etc.

’polar’: Polar subplot for scatterpolar, barpolar, etc.

# can add this later
’map’: Map subplot for scattermap
’mapbox’: Mapbox subplot for scattermapbox

"""