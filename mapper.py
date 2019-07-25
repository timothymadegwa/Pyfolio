class Mapper:
    def __init__(self):
        self.iterable=[]
        
    def map(self, func, iterable):
        """
        O(N)
        This method maps a given function using the values of an iterable

        Parameters
        ----------
        func : function
            The function that it is to be used to map

        iterable : list, tuple, str
            The iterable to be mapped to a given function

        Returns:
        --------
        list:
            A list of the mapped values
        """

        try:
            ans=[func(x) for x in iterable]
        except TypeError:
            ans='Ensure that you enter an iterable object (list, tuple or str) of the right type with regards to the function used'
        return ans


