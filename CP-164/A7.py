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
        return
    
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
        return
    
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
            output+= str(current_node._data)+','
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
            index += 1

        if current is None:
            index = -1
            previous = None

        return previous, current, index
        
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
        return i < self._count and i >= self._count*-1

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

        # Find the last node in the list
        while current is not None:
            previous = current
            current = current._next_node

        # Case 1:linked list is empty
        #    insert into the front of the list
        if previous is None:
            new_node = Node(deepcopy(value), self._front)
            self._front = new_node
        # Case 2: linked list has multiple items
        else:
            new_node = Node(deepcopy(value),current)
            previous._next_node = new_node
        self._count += 1
        return
    
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
    
    """---------------------- Task 1 ----------------------"""
    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            Finds, removes and return copy of linked list item at
            position i
            if invalid index or empty list, print error message and
                return None
        Assert: i is an integer
        Use: item = list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)        
        -------------------------------------------------------
        """
        assert isinstance(i,int),'invalid i'
        if self._front is None:
            print('Error(linked_List.pop): invalid i')
            return None
         
        else:
            previous = None
            current = self._front
            j = 0
            if i<0:
                i = i+self._count
            if i < self._count and i>=0:
                while j<i:
                    
                    previous = current 
                    current = current._next_node
                    j+=1
                item = current._data 
                self._count-=1
                if previous is None:
                    self._front = self._front._next_node
                else:
                    previous._next_node = current._next_node
            else:
                print('')
                return None 
        return deepcopy(item)
    
    """---------------------- Task 2 ----------------------"""
    def swap(self, i, j):
        """
        -------------------------------------------------------
        Description:
            swap items at index i with item at index j
            If either i,j is an invalid index, print error message and do nothing
            if i and j are equal do nothing
            if empty list print error message and return
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            i: index of first swapping item (int)
            j: index of second swapping item (int)
        Returns:
            no returns        
        -------------------------------------------------------
        """
        assert isinstance(i,int) or isinstance(j,int),'invalid i or j'
        if self.is_empty():
            print('Error(Linked_List.swap): empty linked list')
            return 
        if not self._is_valid_index(i) or not self._is_valid_index(j):
            print('Error(Linked_List.swap): invalid i or j')
        
        else:
            if i < 0 or j < 0:
                i = i+self._count 
                j = j+self._count
                
            if (i < self._count and i>=0) or (j < self._count and j>=0):
                current = self._front 
                previous = None
                count_i = 0
                count_j = 0
                
                while count_i<i:
                    previous = current 
                    current = current._next_node
                    count_i+=1
                    
                item_i = deepcopy(current._data)
                current = self._front 
                previous = None 
                
                while count_j<j:
                    previous = current 
                    current = current._next_node
                    count_j+=1
                    
                item_j = deepcopy(current._data)
                previous_i,current_i,_ = self._linear_search(item_i)
                previous_j,current_j,_ = self._linear_search(item_j)
                current_i._data = item_j
                current_j._data = item_i
        return
    
    """---------------------- Task 3 ----------------------"""
    def split(self):
        """
        -------------------------------------------------------
        Description:
            Splits list into two parts. 
            listA contains the first half, listB the second half.
            current list becomes empty
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            listA - a new List with >= 50% of the original List (Linked_List)
            listB - a new List with <= 50% of the original List (Linked_List)
        -------------------------------------------------------
        """
        
        listA = Linked_List()
        listB = Linked_List() 
        if self._count//2 == 0:
            count_even_low1 = 0
            count_even_max1 = self._count//2
            previous1 = None 
            current1 = self._front
            while count_even_low1!=count_even_max1:
                item = current1._data
                listA.append(deepcopy(item))
                self._count-=1
                if previous1 is None:
                    self._front = current1._next_node
                else:
                    current1 = current1._next_node
                count_even_low1+=1
            
            count_even_low2 = 0
            count_even_max2 = self._count
            previous1 = None 
            current1 = self._front
            while count_even_low2!=count_even_max2:
                item = current1._data
                listA.append(deepcopy(item))
                self._count-=1
                if previous1 is None:
                    self._front = current1._next_node
                else:
                    current1 = current1._next_node
                count_even_low2+=1
        else:
            count_odd_low1 = 0
            count_odd_max1 = (self._count//2)+1
            previous1 = None 
            current1 = self._front
            while count_odd_low1!=count_odd_max1:
                item = current1._data
                listA.append(deepcopy(item))
                self._count-=1
                if previous1 is None:
                    self._front = current1._next_node
                else:
                    current1 = current1._next_node
                count_odd_low1+=1
            
            count_odd_low2 = 0
            count_odd_max2 = self._count
            previous1 = None 
            current1 = self._front
            while count_odd_low2!=count_odd_max2:
                item = current1._data
                listA.append(deepcopy(item))
                self._count-=1
                if previous1 is None:
                    self._front = current1._next_node
                else:
                    current1 = current1._next_node
                count_odd_low2+=1
    
        return listA,listB

    """---------------------- Task 4 ----------------------"""
    def union(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            appear in either current linked list and given linked list 
            or appear in both linked lists
            items from current list are added before items from list2
            Current and input linked lists are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.union(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of union (Linked_List)
        -------------------------------------------------------
        """
        assert isinstance(list2,Linked_List),'invalid list'
        list3 = Linked_List()
        current1 = self._front
        previous1 = None 
        while current1 is not None:
            item = current1._data 
            _,current_search1,_ = list3._linear_search(item)
            if current_search1 is None:
                list3.append(deepcopy(item))
            previous1 = current1 
            current1 = current1._next_node
        current2  = list2._front 
        previous2 = None 
        count = 0
        while current2 is not None:
            item  = current2._data
            _,current_search2,_ = list3._linear_search(item)
            if current_search2 is None:
                list3.append(deepcopy(item))
            previous2 = current2 
            current2 = current2._next_node
            count+=1
        return list3

    """---------------------- Task 5 ----------------------"""
    def combine(self,list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            contain all items from current list and given list
            duplicates allowed
            Current items are added before list2 items
            Current and list2 become empty
        Assert: list2 is of type Linked_List
        Use: list3 = list1.cobmine(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of combine (Linked_List)
        -------------------------------------------------------
        """
        assert isinstance(list2,Linked_List),'invalid list'
        list3 = Linked_List()
        temp_list = []
        current1 = self._front 
        previous1 = None 
        while current1 != None:
            item = current1._data 
            list3.append(deepcopy(item))
            prev,curr,_ = self._linear_search(item)
            self._count-=1
            if prev is None: 
                self._front = curr._next_node 
            else: 
                prev._next_node = curr._next_node
#             self._count-=1
#             if previous1 is None:
#                 self._front = current1._next_node
#             else:
#                 current1 = current1._next_node
#             list3.append(deepcopy(item))
            previous1 = current1 
            current1 = current1._next_node
        
        current2 = list2._front 
        previous2 = None 
        while current2 != None:
            item = current2._data 
            list3.append(deepcopy(item))
            prev,curr,_ = list2._linear_search(item)
            list2._count-=1
            if prev is None: 
                list2._front = curr._next_node 
            else: 
                prev._next_node = curr._next_node
#             list2._count-=1
#             if previous2 is None:
#                 list2._front = current2._next_node
#             else:
#                 current2 = current2._next_node
            previous2 = current2
            current2 = current2._next_node
        

        return list3
           
    """---------------- Task 6 -------------------------"""
    def intersection(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains only elements that
            appear in both lists, no duplicates
            Current items are added before list2 items
            Current list1 and list2 are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.intersection(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of intersection (Linked_List)
        -------------------------------------------------------
        """
        assert isinstance(list2,Linked_List),'invalid list'
        list3 = Linked_List()
        current1 = self._front
        previous1 = None 
        while current1 is not None:
            item = current1._data 
            _,current_search1,_ = list2._linear_search(item)
            _,current_search2,_ = list3._linear_search(item)
            if (current_search1 is not None) and (current_search2 is None):
                list3.append(deepcopy(item))
            previous1 = current1 
            current1 = current1._next_node

        return list3