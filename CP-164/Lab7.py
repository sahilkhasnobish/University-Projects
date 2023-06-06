"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from copy import deepcopy
from stack import Stack
class List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Array Implementation
    ----------------------------------------------
    """
    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty list
        Assert: none
        Use: my_list = List()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type List       
        -------------------------------------------------------
        """
        self._items = []
    
    def append(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the list
        Assert: none
        Use: list1.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to list
        Returns:
            No returns        
        -------------------------------------------------------
        """
        self._items += [deepcopy(item)]
        return
    def find(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and returns a copy of item in list that matches key.
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
        i = self._linear_search(key)
        if i != -1:
            return deepcopy(self._items[i])
        else:
            None
        return deepcopy(self._items[i]) if i!=-1 else None
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of the list (str)
        -------------------------------------------------------
        """
        if self.is_empty():
            return '[]'
        output = '['
        for item in self._items:
            output+= str(item)+','
        return output[:-1] + ']'    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return len(self) == 0
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the        
        -------------------------------------------------------
        """
        return len(self._items)
    def __iter__(self):
        """
        -------------------------------------------------------
        Description:
            Generates a Python iterator.
            Iterates from item at index 0 to end of list
        Assert: none
        Use: for item in list1:
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            item - the next value in the list (?)
        -------------------------------------------------------
        """
        for item in self._items:
            yield item
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
        assert isinstance(i,int), 'invalid i'
        return i < len(self) and i>= len(self)*-1
    def insert(self, i, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into the list at index i
            If invalid index assert
        Assert: i is an integer
        Use: list1.insert(i,item)
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            item - an item to be added (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert isinstance(i,int), 'invalid i'
        if self._is_valid_index(i):
            self._items = self._items[:i]+[deepcopy(item)]+self._items[i:]
        else:
            self._items += [deepcopy(item)]
    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in list that matches key.
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
        if self.is_empty():
            print('Error(List.remove): Cannot remove from an empty list')
            return None
        i = self._linear_search(key)
        if i == -1:
            item = None
        else:
            item = deepcopy(self._items[i])
            self._items = self._items[:i]+self._items[i+1:]
        return item
    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            removes item at position i and return a copy
            If invalid index, print error message and return None
        Assert: no asserts
        Use: list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)    
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.pop): List is empty')
            return None
        if not self._is_valid_index(i):
            print('Error(List.pop): Invalid value of i')
            return None
        return self.remove(self._items[i])
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: indx = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            indx: position of key in the list (int)
        -------------------------------------------------------
        """
        indx = -1
        for i in range(len(self)):
            if self._items[i] == key:
                indx = i
                break
        return indx
    """---------------------- Task 1 ------------------------"""
    def extend(self,list2):
        """
        -------------------------------------------------------
        Description:
            append list2 to the current list
            if given parameter is not of type List, 
                print error message and return
        Assert: none
        Use: list1.extend(list1)
        -------------------------------------------------------
        Parameters:
            list2: a List object to be appended to current list(List)
        Returns:
            No returns
        -------------------------------------------------------
        """
        if not isinstance(list2, List):
            print('Error, invalid list.')
        else:
            for i in list2:
                self.append(i)
            list2 = deepcopy(self._items)
            return list2
    
    """---------------------- Task 2 ------------------------"""
    def swap(self, i, j):
        """
        -------------------------------------------------------
        Description:
            Swaps item at position i with item at position j
            if invalid i or j print error message
        Assert: assert i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            i: index of first swap item (int)
            j: index of second swap item(int)
        Returns:
            No returns
        -------------------------------------------------------
        """
        assert isinstance(i,int) and isinstance (j,int)
        if abs(i)>len(self._items):
            print('Error(List.swap): invalid i')
        elif abs(j)>len(self._items):
            print('Error(List.swap): invalid j')
        else: 
            item_i = self._items[i]
            item_j = self._items[j]
            self._items[i] = deepcopy(item_j)
            self._items[deepcopy(j)] = deepcopy(item_i)
        return
    
    """---------------------- Task 3 ------------------------"""
    def remove_many(self, key):
        """
        -------------------------------------------------------
        Description:
            Remves all items in list which match given key
            if list is empty, print error message and return
            Returns a single copy of removed itemd
            if item not found prints an error message and return None
        Assert: no asserts
        Use: item = list1.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key: partial data (?)
        Returns:
            item: copy of removed item (?)
        -------------------------------------------------------
        """
        if self._items == []:
            print('Error(List.remove_many): list is empty')
            return 
        else:
            item = ''
            count = 0
            if key in self:
                while count!=len(self): 
                    if key in self:
                        indx = self._linear_search(key)
                        item = self._items[indx]
                        self.remove(key)
                    count+=1
            else:
                print('Error(List.remove_many): key not found')
                return None
        return deepcopy(item)
    
    """---------------------- Task 4 ------------------------"""
    def split(self):
        """
        -------------------------------------------------------
        Description:
            Splits list into two parts. 
            ls contains the first half,
            rs the second half. 
            Current list becomes empty.
            If current list is empty, print error message 
                and return two empty lists
        Use: ls, rs = l.split()
        Assert: no asserts
        Use: ls,rs = list1.split()
        -------------------------------------------------------
        Parameters:
            no parameters
        Returns:
            ls - a new List with >= 50% of the original List (List)
            rs - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        if self._items!= []:
            half = len(self._items)//2
            upper_half = len(self)-half
            lower_half = half+1
            ls = List()
            rs = List()
            if len(self)%2 == 0:
                    
                first_half = deepcopy(self._items[:half])
                second_half = deepcopy(self._items[half:])
                for i in first_half:
                    ls.append(i)
                for n in second_half:
                    rs.append(n)
                self._items = []
            else:
                first_half = deepcopy(self._items[:upper_half])
                second_half = deepcopy(self._items[lower_half:])
                for i in first_half:
                    ls.append(i)
                for n in second_half:
                    rs.append(n)
                self._items = []
        else:
            ls = []
            rs = []
        return ls,rs
    
    """---------------------- Task 5 ------------------------"""
    def reverse(self):
        """
        -------------------------------------------------------
        Description:
            Reverses the order of elements in the list
            if list is empty do nothing
        Use: ls, rs = l.split()
        Assert: no asserts
        Use: list1.reverse()
        -------------------------------------------------------
        Parameters:
            no parameters
        Returns:
            no returns
        -------------------------------------------------------
        """
        if not self._items == []:
            stack = Stack()
            for i in self:
                stack.push(deepcopy(i))
            self._items = []
            while not stack.is_empty():
                item = stack.pop()
                self.append(deepcopy(item))
        return
    
    """---------------------- Task 6 ------------------------"""
    def __add__(self,list2):
        """
        -------------------------------------------------------
        Description:
            Overloads + operator to allow list1 + list2
            contents of list1 and list2 is not changed
        Assert: list2 is of type List
        Use: list3 = list1 + list2
        -------------------------------------------------------
        Parameters:
            list2: a List object to be added to current list(List)
        Returns:
            list3: result of list1 + list2 (List)
        -------------------------------------------------------
        """
        list1 = deepcopy(self)
        for i in list2:
            list1.append(deepcopy(i))
        list3 = deepcopy(list1)
        return list3