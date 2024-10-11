
class ButtonGen:
    
    def __init__(self, transition_duration:int, frame_duration:int) -> None:
        self.button_wrapper = [
            dict(type='buttons',
                 buttons=[]) # add to these buttons
        ]
        self.transition_duration = transition_duration
        self.frame_duration = frame_duration

    def add_button(self, button_name:str) -> None:

        self.button_wrapper[0]['buttons'] += self(button_name)

    def play_button(self):
        return dict(
                label="Play",
                method="animate",
                args=[None, {'frame': {
                    'duration':self.transition_duration,
                    'transition':{
                            'duration':self.frame_duration,
                            'easing': 'linear'},
                    'redraw':True},
                'fromcurrent':True}]
        )

    def pause_button(self):
        return dict(
                label="Pause",
                method='animate',
                args=[[None], 
                    dict(
                        frame=dict(duration=0, redraw=False),
                        mode='immediate',
                        transition=dict(duration=0)
                )],
            )
    
    # will need to change this 
    def __call__(self, button_name:str) -> dict:
        return getattr(self, button_name)() # params can be added in here when needed
    