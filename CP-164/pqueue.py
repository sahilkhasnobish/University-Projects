"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""

#------------------------------
# CP264 Winter 2020
# Week 5 - R5
# Prioirty Queue - Array Based solution
#------------------------------
from copy import deepcopy

class pQueue:
    """
    -------------------------------------------------------
    Implementation of Prioirity Queue ADT (Array-based Implementation)
    unsorted insert approach
    Highest priority is determined to be greatest item
    If multiple highest items, pick the one that arrived earlier
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Priority Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum size of queue (default = 10)
        Returns:
            A pQueue object (pQueue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._items = []
        self._size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of highest priority item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """

        if self.is_empty():
            print('Error(pQueue.peek): Invalid peek operation. Queue is empty')
            return None
        highest = 0
        for i in range(1,len(self._items)):
            if self._items[i] > self._items[highest]:
                highest = i
        return deepcopy(self._items[highest])
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the priority queue
        Use: queue.insert(item)
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(pQueue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.append(deepcopy(item))
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the item with the highest priority from the queue
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - highest priority item in the queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.remove):Invalid remove operation. Queue is empty')
            return None
        highest = 0
        for i in range(1,len(self._items)):
            if self._items[i] > self._items[highest]:
                highest = i
        return deepcopy((self._items).pop(highest))
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return len(self._items) == self._size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return len(self._items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '()'
        else:
            output = '('
            for i in range(len(self._items)):
                output = output + str(self._items[i])+' '
        output = output[:-1]+')'
        return output
    
class pQueue2:
    """
    -------------------------------------------------------
    Implementation of Prioirity Queue ADT (Array-based Implementation)
    Sorted insertion approach
    Highest priority is determined to be greatest item
    If multiple highest items, pick any item
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Priority Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum size of queue (default = 10)
        Returns:
            A pQueue object (pQueue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._items = []
        self._size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of highest priority item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.peek): Invalid peek operation. Queue is empty')
            return None
        return deepcopy(self._items[-1])
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the priority queue
        Use: queue.insert(item)
        Analysis: O(nlogn) - Python uses Timsort which is:
                 O(nlogn) worst and average, O(n) best case
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(pQueue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.append(item)
            self._items = sorted(self._items)
            #self.items.sort()
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the item with the highest priority from the queue
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - highest priority item in the queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.remove):Invalid remove operation. Queue is empty')
            return None
        return deepcopy(self._items.pop(-1))
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return len(self._items) == self._size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return len(self._items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '()'
        else:
            output = '('
            for i in range(len(self._items)-1,-1,-1):
                output = output + str(self._items[i])+' '
        output = output[:-1]+')'
        return output
 
class pQueue3:
    """
    -------------------------------------------------------
    Implementation of Prioirity Queue ADT (Array-based Implementation)
    unsorted insert approach
    Supports highest value as top priority, or lowest value as top priority
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self,size=DEFAULT_SIZE,mode = 'H'):  #<------ edit this function
        """
        -------------------------------------------------------
        Description:
            Initializes a Priority Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum size of queue (default = 10)
        Returns:
            A pQueue object (pQueue)            
        -------------------------------------------------------
        """
        assert isinstance(size,int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        assert mode == 'H' or mode == 'L', 'unsupported priority'
        self._items = []
        self._size = size
        self._mode = mode
        
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of highest priority item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.peek): Invalid peek operation. Queue is empty')
            return None
        highest = 0
        if self._mode == 'H':
            for i in range(1,len(self.items)):
                if self.items[i] > self._items[highest]:
                    highest = i
        elif self._mode == 'L':
            for i in range(1,len(self.items)):
                if self.items[i] < self._items[highest]:
                    highest = i
        return deepcopy(self._items[highest])
    
    def insert(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the priority queue
        Use: queue.insert(item)
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(pQueue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.append(deepcopy(item))
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the item with the highest priority from the queue
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - highest priority item in the queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.remove): Invalid remove operation. Queue is empty')
            return None
        highest = 0
        if self._mode == 'H':
            for i in range(1,len(self._items)):
                if self._items[i] > self._items[highest]:
                    highest = i
        elif self._mode == 'L':
            for i in range(1,len(self._items)):
                if self._items[i] < self._items[highest]:
                    highest = i
        return deepcopy(self._items.pop(highest))
        
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._items)== 0
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return len(self._items) == self._size
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return len(self._items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue in priority order
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self.is_empty():
            output =  '()'
        else:
            output = '('
            if self._mode == 'H':
                for i in range(len(self._items)-1,-1,-1):
                    output = output + str(self._items[i])+' '
            elif self._mode == 'L':
                for i in range(len(self._items)):
                    output = output + str(self._items[i])+' '
        output = output[:-1]+')'
        return output
        