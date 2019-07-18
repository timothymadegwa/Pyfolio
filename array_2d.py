class Array:
    def __init__(self):
        self.row=0
        self.col=0

    def create_array(self, row,col):
        """
        This method creates an array with row number of rows and col number of columns
        
        Parameters
        ----------
        row : int
            The number of rows of the 2D matrix to be formed
            
        col : int
            The number of columns of the 2D matrix to be formed
             
        Returns
        -------
        Array
            A 2D array of 0's
        """
        
        self.row=row
        self.col=col
        self.array=[[0 for _ in range(col)] for _ in range(row)]
        return self.array
    
    def shape(self):
        """
        This method return the number of rows and columns of the 2D array
        
        Returns
        -------
        Tuple:
            A tuple containing the number of rows and columns
        """
        return (self.row, self.col)

    def clear_array(self, value):
        """
        This method clears the array with the arguement value

        Parameter:
        ----------
        value : int, float, str
            The value to be filled in when clearing the array

        Returns:
        --------
        Array
            An array filled with the replacement value
        """
        self.array=[[value for _ in range(self.col)] for _ in range(self.row)]
        return self.array

    def get_element(self,row ,col):
        """
        This method gets the element in the specified row and column

        Parameters:
        -----------
        row : int
            The row to accessed
        col : int
        The column to be accessed

        Returns:
        --------
        int, float, str
        The value of the selected element in the array
        """
        if (row > self.row) or (col > self.row):
            raise IndexError('Index is out of Range')
        return self.array[row][col]

    def set_element(self, row, col,value):
        """
        This method sets the element of a selected row and column
        
        Parameters:
        -----------
        row : int
            The row to accessed
        col : int
        The column to be accessed
        value : int,float,str
            the value to be inserted

        Returns:
        --------
        Array
        The array with the value replaced
        """
        if (row > self.row) or (col > self.row):
            raise IndexError('Index is out of Range')
        else:
            self.array[row][col]=value
        return self.array

'''

a=Array()
arr=a.create_array(4,3)
shape=a.shape()
cle=a.clear_array(5)
ele=a.get_element(1,1)
st=a.set_element(1,2,8)
print(shape)
print(arr)
print(cle)
print(ele)
print(st)
'''