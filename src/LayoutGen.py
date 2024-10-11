import plotly.graph_objects as go

import schemas


class LayoutGen:
    # don't forget to add 
    def polar(self, params:schemas.ScatterPolarIn) -> go.Layout:
        return go.layout.Polar(

            radialaxis=dict(
                range=params.radial_range, 
                showticklabels=params.radial_ticklables, 
                ticks=params.radial_ticks),

            angularaxis=dict(
                showticklabels=params.angular_ticklabels, 
                ticks=params.angular_ticks,
                rotation=params.angular_rotation), 
                domain={'x' : params.x_domain, 'y' : params.y_domain}
        )
    
    def scene(self, params:schemas.Scatter3dIn) -> go.layout.Scene:

        return go.layout.Scene(
            xaxis=dict(
                nticks=params.xaxis_nticks,
                range=params.xaxis_range
            ),
            yaxis=dict(
                nticks=params.xaxis_nticks,
                range=params.xaxis_range
            ),
            zaxis=dict(
                nticks=params.xaxis_nticks,
                range=params.xaxis_range
            ),
            aspectratio = {'x':1,'y':1,'z':1},
            domain={'x' : params.x_domain, 'y' : params.y_domain}
        )

    # unsure if this is the move
    def __call__(self, method:str, params) -> go.Layout:
        return getattr(self, method)(params)