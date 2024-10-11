import schemas


class Specs:
    # specs could be inferred from position in list
    def __init__(self, params:schemas.FrameIn) -> None:

        # FrameIn Parameters
        self.params=params.params

        # same plots should have the same axis type
        # get each unique row/column pair
        self.row_col = set([
            (i.row, i.column, i.spec, i.rowspan, i.colspan) 
             for i in self.params])
        
        # get specs from calling method
        self.specs = self.get_specs()
    
    def get_specs(self) -> list[list[dict]]:
        
        # get max number of rows and columns
        nrows = max([i[0] for i in self.row_col])
        ncols = max([i[1] for i in self.row_col])

        # create empty list of dictionaries as an empty spec
        specs = [[{} for i in range(ncols)] for j in range(nrows)]
        
        # iterate over row_column pairs
        for i in self.row_col:
            # index parameters
            # check if it has the same row and column

            # overwrite temp specs values with parameter values
            specs[i[0]-1][i[1]-1] = { # set row column
                'type': i[2],
                'rowspan' : i[3],
                'colspan' : i[4]
                }

        # return 2d list of dicts
        return specs