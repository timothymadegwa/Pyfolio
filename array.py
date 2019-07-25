class Array:
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def length(self):
        """
        O(1)

        This method gets the shape(length) of the array

        Returns:
        --------
        tuple
        A tuple with the shape of the array
        """
        return (1,self.size)

    def get_element(self, index):
        """
        O(N)

        This method gets the element in the specified index

        Parameters:
        -----------
        index : int
            The index to accessed

        Returns:
        --------
        int, float, str
        The value of the selected element in the array
        """
        if index > self.size:
            raise Exception('Index out of range')
        else:
            self.element=self.array[index]
        return self.element

    def add_element(self, index, element):
        """
        O(N)
        
        This method adds the element in the specified index

        Parameters:
        -----------
        index : int
            The index to accessed
        element : int, float, str
        The element to be added

        Returns:
        --------
        list
        The list with the element inserted
        """
        if index>self.size:
            raise Exception('Index out of range')
        else:
            self.array[index] = element
        return self.array
