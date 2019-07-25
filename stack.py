class Stack:
    def __init__(self):
        """
        This instanciates the class.
        """
        self.items = []

    def is_empty(self):
        """
        O(1)
        This method is meant to check whether the stack is empty 

        returns
        -------
        A boolean (False) if it is not empty
        
        """
        if len(self.items) == 0:
            return True
        else:
            return False

    def length(self):
        """
        O(N)
        checks the number of elements in the stack

        returns
        -------
        no of elements in the stack
        
        """
        return len(self.items)
    
    def push(self, item):
        """
        O(1)
        This method is meant to push or rather add items to the stack

        Parameters
        ----------
        item : entity to be added to the stack

        returns
        -------
        List

            The stack with the item added to it
        """
        return self.items.append(item)

    def pop(self, item):
        """
        O(N)
        This method is meant to pop or rather remove items from the stack

        Parameters
        ----------
        item : entity to be removed from the stack

        returns
        -------
        List

            The stack with the item removed from it
        """
        if(self.is_empty == True):
            raise ValueError("The stack is empty hence cannot pop any item from it")

        return self.items.pop(item)

    def top(self):
        """
        O(N)
        This method is return the topmost element

        returns
        -------
        List
            the topmost element

        """
        if(self.is_empty == True):
            raise ValueError("The stack is empty cannot return the topmost value")
        else:
            return self.items[-1]



