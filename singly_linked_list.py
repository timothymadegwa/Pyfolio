class Stack:
    class Node:
        """
        create a node
        """

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        """
        contents of the node
        
        """
        self.head = None
        self.size = 0

    def len(self):
        """
        O(N)
        checks the number of elements in the list

        returns
        -------
        no of elements in the list

        """
        return self.size

    def is_empty(self):
        """
        O(1)
        This method is meant to check whether the list is empty

        returns
        -------


        """
        return self.size == 0

    def push(self, element):
        """
        O(1)

        add a node to the stack

        Parameters
        ----------
        element : node to be added
        
        """
        self.head = self.Node(element, self.head)
        self.size += 1

    def peek(self):
        """return element at the top of the stack"""
        if self.is_empty:
            raise Exception("Stack is Empty")
        else:
            return self.head.element

    def pop(self):
        """
        O(N)
        remove the top node of the stack

        Returns
        -------
        List
            The stack with the item removed from it
        """
        if self.is_empty:
            return Exception("Stack is empty")
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer
