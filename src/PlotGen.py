import plotly.graph_objects as go
import schemas


# we could make an iterable wrapper of this
class PlotGen:
    def make_scatter(
            self, params:schemas.ScatterIn
            ) -> go.Scatter:
        """
        x: iterable sequence
        y: iterable sequence
        mode: linemode for plot

        returns go.Scatter graph object
        """
        # slice data 
        
        x = self._slice_data(params.x, params.split)
        y = self._slice_data(params.y, params.split)

        return go.Scatter(
            x=x,
            y=y,
            mode=params.mode,
        )
    
    def make_scatterpolar(
            self, params:schemas.ScatterPolarIn
            ) -> go.Scatterpolar:
        """
        theta: categories or degree values
        r: data values representing the intensity of the wave
        name: name of the plot
        fill: fill type

        returns go.Scatterpolar graph object
        """
        # slice data 
        data = self._slice_data(params.r, params.split)
        return go.Scatterpolar(
            r=data,
            theta=params.theta,
            fill=params.fill,
            name=params.name,

        )
    
    def make_scatter3d(self, params:schemas.Scatter3dBase) -> go.Scatter3d:
        """# Add docstrings here later!"""
        # add slicing of data
        # change this to be a dataframe to avoid this later
        data = self._slice_data(params.xyz, params.split)
        return go.Scatter3d(
            x=data.iloc[:,0], y=data.iloc[:,1], z=data.iloc[:,2],
            mode=params.mode, 
            marker = dict(
                size = params.marker.size,
                color = params.marker.color,
                colorscale = params.marker.colorscale,
                opacity = params.marker.opacity,
            )
        )
    
    def make_pie(self, params:schemas.PieBase) -> go.Pie:
        """# Add docstrings here later!"""
        
        return go.Pie(
            # data
            labels=params.labels,
            values=params.values,
            # graph text
            hoverinfo=params.hoverinfo,
            textinfo=params.textinfo,
            # figure name
            name=params.name,
            # graph stype info
            marker=dict(
                colors = params.marker.colors,
                line=dict(
                    color = params.marker.line_color,
                    width = params.marker.line_width
                ),
            ),
        )
    
    def make_surface(self, params:schemas.SurfaceIn):
        """# Add docstrings here later!"""
        data = self._slice_data(params.xyz, params.split)
        return go.Surface(
            x=data.columns, 
            y=data.index,
            z=data,
            showscale=False
        )

    # this should slice data
    def make_plot(self, params): # its not a dict!
        return getattr(self, f'make_{params.plottype}')(params)

    def _slice_data(self, data, splits:tuple):
        return data[splits[0]:splits[1]]
        

    # stacked polarscatter should go here 