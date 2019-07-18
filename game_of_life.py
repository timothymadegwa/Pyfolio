class GameOfLife:
    def __init__(self,row=4,col=4):
        self.row=row
        self.col=col
        self.game=[[None for _ in range(self.col)] for _ in range(self.row)]

    def create_game(self, one, two, three):
        """
        This function creates the array containing the living cells by parsing in 3 tuples for
        the positions of the living cells
        """
        self.x1, self.x2=one
        self.y1, self.y2=two
        self.z1, self.z2=three
        self.game[self.x1][self.x2], self.game[self.y1][self.y2], self.game[self.z1][self.z2] = 1,1,1
        return self.game