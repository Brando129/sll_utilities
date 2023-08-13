"""Add a method contains(value) to your SLL class,
which is given a value as a parameter.  Return
a boolean (true/false); true, if the list possesses
a node that contains the provided value."""

"""Create a new SLL method length() that returns
number of nodes in that list."""

"""Create display() that returns a string containing all list values."""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def contains(self, val):
        runner = self.head
        while(runner):
            if runner.val == val:
                return True
            runner = runner.next
        return False

    def length(self):
        runner = self.head
        length = 0
        while(runner):
            length+=1
            runner = runner.next
        return length

    def display(self):
        runner = self.head
        str = ''
        while(runner):
            str += f'{runner.val}  -->'
            runner = runner.next
        return str