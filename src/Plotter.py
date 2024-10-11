
from plotly.subplots import make_subplots

from src.Specs import Specs
from src.FrameGen import FrameGen
from src.ButtonGen import ButtonGen
from src.LayoutGen import LayoutGen

from src.helper import create_typename

import schemas

class Plotter:

    def new_animation(self, rows:int, cols:int, fg_params:schemas.FrameIn):
        
        # create subplots object
        fig = make_subplots(
            # set number of rows and columns
            rows=rows, cols=cols,

            # set subplot titles from figure parameters
            subplot_titles=[i for i in fg_params.subplot_titles],
            # do not share axes 
            shared_xaxes = False, shared_yaxes = False,

            # set specs using Specs object
            specs = Specs(fg_params).specs
        )    # GENERATORS

        # add frame generator
        gen = FrameGen(
            parameters=fg_params,
        ) 

        # add frame layout generator
        layoutgen = LayoutGen()

        # add button generator and create buttons
        buttongen = ButtonGen(
            0,0 # change these to come from parameters
        )
        for i in ['play_button', 'pause_button']: # add buttons 
            buttongen.add_button(i)

        # FRAME GENERATION

        # add initial coordinates
        for param in fg_params.params:
            # check if plot should be animated
            if param.animate:

                # overwrite default (0,-1) splits from frame
                param.split = (
                    fg_params.slices[0][0], fg_params.slices[0][1]
                )
                # add trace to the plot
                fig.add_trace(
                    gen.make_plot(param), row=param.row, col=param.column
                )
            else:
                # add trace without any slicing
                fig.add_trace(
                    gen.make_plot(param), row=param.row, col=param.column
                )
        
        # initialize for recursive parsing
        typenames = []

        # parse parameters
        for param in fg_params.params:
            # check for axis override flag
            if param.manual_axis:

                # infer layout name by recursively parsing typenames
                typename = create_typename(typenames, param.axis_name)
                
                # save pregenerated domain from overwriting 
                param.x_domain = fig.layout[typename]['domain']['x']
                param.y_domain = fig.layout[typename]['domain']['y']

                # update axis layout  
                fig.layout[typename] = layoutgen(param.axis_name, param)


        # init timer without iterating
        fig.update_layout(
            title=gen.timer.get_time()
        ) 

        # generate frames
        fig.frames = gen.gen_frames()
        
        # update layout with buttons and DARK template
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                buttons = [buttongen(name) 
                            for name in ['play_button','pause_button']],
            )],
            template='plotly_dark',
        )

        fig.show()