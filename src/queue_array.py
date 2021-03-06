"""
-------------------------------------------------------
queue_array.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-01-24
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty queue.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = q.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = q.is_full()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: q.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the queue.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = q.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of the queue - the value is
            removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        value = self._values.pop(0)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = q.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of the queue -
            the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])

        return value

    def combine(self, q2):
        """
        -------------------------------------------------------
        Combines contents of two queues into a new queue.
        Use: q3 = q1.combine(q2)
        -------------------------------------------------------
        Preconditions:
            q2 - an array-based queue (Queue)
        Postconditions:
            returns
            q3 - Contents of self and q2 are interlaced 
                into q3 (Queue)
        -------------------------------------------------------
        """

        return q3

    def split(self):
        """
        -------------------------------------------------------
        Splits a queue into two other queues with values 
        alternating between target queues.
        Use: q2, q3 = q1.split()
        -------------------------------------------------------
        Postconditions:
            returns
            q2 - a target (Queue)
            q3 - a second target (Queue)
            Contents of the current queue are moved alternately 
            to q2 and q3. Current queue is empty.
        -------------------------------------------------------
        """

        return q2, q3

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def identical(self, q2):
        """
        ----------------
        Determines whether two given queues are identical.
        Entries of q1 and q2 are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: b = q1.identical(q2)
        ---------------
        Preconditions:
            q2 - a queue object (Queue)
        Postconditions:
            returns
            is_identical - True if q1 and q2 are identical, False otherwise. 
                Queues are unchanged. (boolean)
        ---------------
        """
        is_identical = True
        n = 0

        if len(self._values) != len(q2._values):
            is_identical = False
        elif (len(self._values) != 0 and len(q2._values) == 0) or (len(self._values) == 0 and len(q2._values) != 0):
            is_identical = False
        else:
            while n <= (len(self._values) - 1):
                if self._values[n] == q2._values[n]:
                    pass
                else:
                    is_identical = False
                n += 1

        return is_identical
