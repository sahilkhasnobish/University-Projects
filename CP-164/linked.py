"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""

from copy import deepcopy

class Node:
    """
    ----------------------------------------------
    Implementation of a Linked List node
    ----------------------------------------------
    """
    def __init__(self, item, next_node):
        """
        -------------------------------------------------------
        Description:
            Creates and initializes an empty linked list node
            data and next set to given values
        Assert: none
        Use: my_node = Node()
        -------------------------------------------------------
        Parameters:
            item: An arbitrary object (?)
            next_node: reference to another node
        Returns:
            An object of type Node 
        -------------------------------------------------------
        """ 
        self._data = deepcopy(item)
        self._next_node = next_node
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns string representation of node
            Used for testing purposes
        Assert: none
        Use: str(my_node) or print(my_node)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string represenation of node 
        -------------------------------------------------------
        """
        return str(self._data)


class Linked_List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Linked List Implementation
    ----------------------------------------------
    """
    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty linked list
            head is initialized to None
        Assert: none
        Use: my_list = Linked_list()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type Linked_List       
        -------------------------------------------------------
        """ 
        self._front = None 
        self._count = 0
        

    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if linked list is empty
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return self._front is None 

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items in a list
            same as number of nodes
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the linked list       
        -------------------------------------------------------
        """
        return self._count
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in linked list.
            If list is empty, prints error message and returns None
        Assert: none
        Use: item = list1.peek()
        -------------------------------------------------------
        Parameters:
            No parametrs
        Returns:
            item: copy of first tiem in linked list (?)
        -------------------------------------------------------
        """
        if self._front is None:
            print('Error(Linked_List.peek): Cannot peek at an empty list')
            return None
        return deepcopy(self._front._data)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of linked list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of linked list (str)
        -------------------------------------------------------
        """
        if self._front is None:
            return '[]'
        output = '['
        current_node = self._front
        while current_node is not None:
            output+=str(current_node._data)+','
            current_node = current_node._next_node
        return output[:-1]+']'
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the linked list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: p, c, i = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            p: pointer to the node previous to the one containing key (Node)
            c: pointer to the node containing the key (Node) 
            i: index of the node containing key (int)
        -------------------------------------------------------
        """
        previous = None 
        current = self._front
        index = 0
        while current is not None and current._data != key:
            previous = current 
            current = current._next_node 
            index+=1
        if current is None:
            index = -1
            previous = None 
        return previous, current,index
    
    def index(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds location of first item matching key in linked list.
            Returns the position of the item that match given key
            Returns -1 if not found
        Assert: No asserts
        Use: i = list1.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - location of key in the linked list (int)
        -------------------------------------------------------
        """
        _,_,i = self._linear_search(key)
        return i
    
    def find(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and returns a copy of item in linked list that matches key.
            If item not found returns None
        Assert: none
        Use: item = list1.find(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        _,current,_ = self._linear_search(key)
        if current is not None:
            item = deepcopy(current._data)
        else:
            item = None 
        return item
    
    def __contains__(self, key):
        """
        -------------------------------------------------------
        Description:
            Returns True if linked list contains an item that
                matches given key, returns False otherwise
        Assert: none
        Use: result = key in list1
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            result: True/False
        -------------------------------------------------------
        """
        previous,current,i = self._linear_search(key)
        return current is not None
    def append(self, value):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the linked list
        Assert: none
        Use: my_list.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to linked list (?)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        #find the last node in the last
        while current is not None:
            previous  = current
            current = current._next_node
        #case 1: linked list is empty: insert into the front of the linked list 
        if previous is None:
            new_node = Node(deepcopy(value),None)
            self._front = new_node
        #case 2: linked list is not empty: insert at the end 
        else:
            new_node = Node(deepcopy(value),None)
            previous._next_node = new_node
        self._count+=1
        return 
       
    def insert(self, i, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into the linked list at index i
            works for positive and negative values of i
            if i is outside the range of indices --> append
        Assert: i is an integer
        Use: list1.insert(i,item)
        -------------------------------------------------------
        Parameters:
            i - position of the given item to be inserted at (int)
            item - an item to be added (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert isinstance(i,int),'invalid i'
        if not self._is_valid_index(i):
            i = self._count #insert at the end 
        elif i < 0:
            i = self._count+i 
        location = 0
        previous_node = None
        current_node = self._front
        while location < i and current_node is not None:
            previous_node = current_node
            current_node = current_node._next_node
            location+=1
        if previous_node is None:
            new_node = Node(item,self._front)
            self._front = new_node
        else:
            new_node = Node(item,current_node)
            previous_node._next_node = new_node
        self._count+=1
        return 

    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in linked list that matches key.
            if key not found returns None
            If list is empty, prints an error message and returns None
        Assert: none
        Use: item = list1.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        if self._front is None: #Case1: list is empty
            print('Error(Linked_List.remove): Cannot remove from an empty linked list')
            return None
        previous,current,_ = self._linear_search(key)
        if current is None: #case2: key not found 
            item = None 
        else:
            item = current._data
            self._count-=1
            if previous is None: #case 3: if first item 
                self._front = current._next_node 
            else: #case 4 if other than first item
                previous._next_node = current._next_node
            
        return item 
    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Description:
            Private helper method to validate an index value
            Valid python list values are -len(list) to len(list)-1
        Assert: i is an integer
        Use: result = self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: True if valid index and False otherwise (bool)        
        -------------------------------------------------------
        """
        assert isinstance(i,int),'invalid i'
        return i < self._count and i>= self._count*-1

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of the ith element of the linked list
        Assert: i is an integer and is a valid index
        Use: item = list1[i]
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: copy of ith element in list (?)      
        -------------------------------------------------------
        """
        assert isinstance(i,int) and self._is_valid_index(i), 'invalid i'
        if i < 0:
            i = self._count + i
        
        j = 0
        current = self._front
        while j < i:
            current = current._next_node
            j+=1
        return deepcopy(current._data)
        
    
    def __iter__(self):
        """
        -------------------------------------------------------
        Description:
            Generates a Python iterator.
            Iterates from head to tail of linked list
        Assert: none
        Use: for item in list1:
        -------------------------------------------------------
        Parameters:
            No parameters
        Yields:
            item - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front
        while current is not None:
            yield current._data
            current = current._next_node

    def count(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds the number of times the given key appears in the linked list
        Assert: list is not empty
        Use: counter = list1.count(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            result: number of ocurrences of key in the list (int)
        -------------------------------------------------------
        """
        assert self._front is not None, "cannot count keys in an empty linked list"
        number = 0
        current = self._front
        while current is not None:
            if key == current._data:
                number+=1
            current = current._next_node
        return number 

    def reverse(self):
        """
        -------------------------------------------------------
        Description:
           reverses the order of items in linked list
        Assert: no asserts
        Use: list1.reverse()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        new_front = None
        while self._front is not None:
            temp = self._front._next_node
            self._front._next_node = new_front
            new_front = self._front
            self._front = temp
        self._front = new_front 
        return 

    def clean(self):
        """
        -------------------------------------------------------
        Description:
            removes all duplicates from the linked list
            The first instance of each duplicate is preserved
        Assert: no asserts
        Use: list1.clean()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        key_node = self._front
        #outer loop: loop though every node-compare with the rest of the list 
        while key_node is not None:
            previous = key_node
            current = key_node._next_node
            #inner loop: search to the end of the list for a duplicate 
            while current is not None:
                #if found remove the item 
                if current._data == key_node._data:
                    self._count-=1
                    previous._next_node = current._next_node
                #if not found check the next node 
                else:
                    previous = current
                #move to the next node (inner loop)
                    current = current._next_node
                
            key_node = key_node._next_node
        return 

    def identical(self, list2):
        """
        -------------------------------------------------------
        Description:
            Check if list2 is identical to current list
            Check if items are equal and in same order
        Assert: list2 is a Linked List
        Use: result = list1.identical(list2)
        -------------------------------------------------------
        Parameters:
            list2: a Linked_List object to compare to current List (Linked_List) 
        Returns:
            True if identical, False otherwise (bool)
        -------------------------------------------------------
        """
        assert isinstance(list2,Linked_List),'invalid list2'
        if self._count!=list2._count:
            return False 
        current1 = self._front
        current2 = list2._front
        while current1 is not None and current1._data == current2._data:
            current1 = current1._next_node
            current2 = current2._next_node
        return current1 is None
