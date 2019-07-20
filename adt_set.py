class Set:
    def __init__(self):
        """
        This instanciates the class
        """
        self.values=[]
        

    def create_set(self, values):
        """
        This method creates a set of values parsed into it

        Parameters:
        -----------
        values: list, tuple, set
            The iterable object that to beused in the creation of the set

        Returns:
        --------
        list:
            A list with unique values of the iterable object parsed in
        """
        my_set=[]
        try:
            for _ in values:
                if _ not in my_set:
                    my_set.append(_)
        except TypeError:
            my_set='Ensure that you enter an iterable object'
        return my_set

    def add(self,set1,val):
        """
        This method adds the val to the set parsed in

        Parameters :
        ------------
        set1 : set instance
            The set you want to add val to
        val: int, float, str, set, list
            The value(s) to be added to the set parsed in the method

        Returns:
        --------
        list:
            The the new list of unique values
        """
        try:
            for _ in val:
                if _ not in set1:
                    set1.append(_)
        except TypeError:
            set1.append(val)
        return set1
    
    def union(self, set1,set2):
        """
        This method returns a union of two sets given to it

        Parameters:
        -----------
        set1: set instance
            A set instance
        set2: set instance
            A set instance

        Returns:
        -------
        list
            A list containing the elements of the union of the two sets
        """
        solution_set=[]
        solution=set1+set2
        try:
            for _ in solution:
                if _ not in solution_set:
                    solution_set.append(_)
        except TypeError:
            solution_set='Ensure that you enter an iterable object'
        return solution_set

    def intersection(self, set1,set2):
        
        """
        This method returns a intersection of two sets given to it (values common in both sets)

        Parameters:
        -----------
        set1: set instance
            A set instance
        set2: set instance
            A set instance

        Returns:
        -------
        list
            A list containing the elements of the intersection of the two sets
        """
        solution_set=[]
        for _ in set1:
            if _ in set2:
                solution_set.append(_)
        return solution_set
    
    def unique(self, set1,set2):
        
        """
        This method returns a unique elements of two sets given to it

        Parameters:
        -----------
        set1: set instance
            A set instance
        set2: set instance
            A set instance

        Returns:
        -------
        list
            A list containing the unique elements of the two sets
        """
        solution_set=[]
        for _ in set1:
            if _ not in set2:
                solution_set.append(_)
        for _ in set2:
            if _ not in set1:
                solution_set.append(_)
        return solution_set
