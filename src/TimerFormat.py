
class TimerFormat:
    
    def __init__(
        self, denominator:int, 
        digit_size:int,
        numerator:int=0
    ) -> None:
        
        self.num, self.den = numerator, denominator
        self.digit_size = digit_size

    def update_time(self, new_numerator:int) -> None:
        self.num=new_numerator

    def get_time(self) -> str:
        return f'{self.num:0{self.digit_size}}/{self.den:0{self.digit_size}}'

    def __call__(self) -> str:

        self.num += 1
        return f'{self.num:0{self.digit_size}}/{self.den:0{self.digit_size}}'
    
    def __repr__(self) -> str:
        return f'Time: {self}'
        
    