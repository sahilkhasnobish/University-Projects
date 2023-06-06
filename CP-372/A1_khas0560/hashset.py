"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from list import List 
class HashSet:
    _DEFAULT_LOAD_FACTOR = 5
    def __init__(self,size,load_factor):
        self.size = size #number of slots 
        self._load_factor = load_factor 
        
        self._table = []
        self._count = 0 
        
        for _ in range(self.size):
            self._table.append(List())
        return 
    def __len__(self):
        return self._count 
    
    def is_empty(self):
        return self._count == 0 
    
    def _find_slot(self,key):
        slot_num = hash(key) % self.size #fix this 
        return self._table[slot_num]
    
    def __contains__(self,key):
        slot = self._find_slot(key)
        return key in slot 
    def find(self,key):
        slot = self._find_slot(key)
        value = slot.find(key)
        return value 
    def insert(self,item):
        slot = self._find_slot(item)
        
        if item in slot: #duplicates not allowed in a hashset
            inserted = False 
        
        else:
            slot.append(item)
            self._count+=1
            inserted = True 
            
            #rehash?
            if self._count > (self._load_factor*self.size):
                self._rehash()
        return inserted 
    def _rehash(self):
        #copy current data to a temporary variable 
        temp_table = self._table 
        
        #increase #slots 
        self.size = self.size * 2 + 1#use odd num of slots 
        
        #create new table and slots 
        self._table = []
        for _ in range(self.size):
            self._table.append(List())
        
        #copy data from temp_table to new table 
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0) #get a slot
            
            while not old_slot.is_empty(): #add items to slots
                item = old_slot.pop(0)
                slot = self._find_slot(item)
                slot.append(item)
        return
    def remove(self,key):
        if self._count == 0: #empty 
            print('Error(HashSet.remove): Cannot remove from an empty hash set')
            return None 
        
        slot  = self._find_slot(key)
        item = slot.remove(key)
        if item is not None:
            self._count -= 1
        return item 
    
    def __iter__(self):
        for slot in self._table:
            for item in slot:
                yield item 
    def __str__(self):
        output = 'Hashset(count) = ' + str(self._count) + '\n'
        i = 0
        for slot in self._table:
            output += "Slot " + str(i) + ": "
            if not slot.is_empty():
                for item in slot:
                    output+=str(item) + ' , '
                output = output[:-3] + '\n'
            else:
                output+='\n'
            i+=1 
        return output 
            
    