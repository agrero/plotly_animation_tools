import plotly.graph_objects as go 

from src.PlotGen import PlotGen 

import schemas

# WE SHOULD CONVERT THIS TO AN ITERABLE WRAPPER OF PLOTS
class FrameGen(PlotGen):
    def __init__(
            self, 
            parameters:schemas.FrameIn,
        ) -> None:
        self.timer = parameters.timer

        # iterable list of parameter data classes
        self.params = parameters.params
        self.slices = parameters.slices 
        
        # empty frames in case you wanna save and load
        self.frames = None

    def gen_frame(self) -> go.Frame:
        """
        params

        ndx: tuple = index tuple pair
        theta: list = list of categories/theta values
        columns: list[str] = list of column names
        """
        return go.Frame(
            # data
            data = [self.make_plot(param) for param in self.params],

            # TRACES 
            traces=[i for i in range(len(self.params))],

            # TIMER
            layout=go.Layout(title=self.timer()),    
        )

    def gen_frames(self) -> list[go.Frame]:
        
        frames = []

        # iterate slices
        for split in self.slices:
            # change split if it its being animated 
            for param in self.params: 

                # check for animation flag
                if param.animate:
                    param.split = split
                    

            # make and append plot  
            frames.append(self.gen_frame())

        # return frames
        return frames    

    