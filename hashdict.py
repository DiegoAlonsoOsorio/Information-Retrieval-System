from dict_abstract import DictAbstract

class ChainingHashTableItem:
    def __init__(self, itemKey, itemValue):
        self.key = itemKey
        self.value = itemValue
        self.next = None

class HashTableDict(DictAbstract):

    def __init__(self, initial_size = 100003):
        self.patient_table = [None] * initial_size
        self.size = 0 
    
    def hashKey(self, key):
        return abs(hash(key))

    # Description, Author: Karan Athwal
    def __len__(self):
        return self.size

    # Description, Author: Karan Athwal
    def __contains__(self, key):
        try:
            self[key]
            return True 
        except KeyError:
            return False

    # Searches the hash table for the given key and returns the corresponding value, Author: Grace Lasiter
    def __getitem__(self, key):
        bucket_index = self.hashKey(key) % len(self.patient_table)
        item = self.patient_table[bucket_index]
        previous = None
        
        while item != None:
            if item.key == key:
                return item.value
            item = item.next
        
        raise KeyError(key)

    # Inserts or updates a key-value pair in the hash table, Author: Grace Lasiter
    def __setitem__(self, key, value):
        bucket_index = self.hashKey(key) %  len(self.patient_table)
        item = self.patient_table[bucket_index]
        previous = None
#add error handling and add index checking for collisons and add bucket checking
        while item != None:
            if item.key == key:
                item.value = value
                return True
            previous = item
            item = item.next
        
        new_item = ChainingHashTableItem(key, value)
        if self.patient_table[bucket_index] == None:
            self.patient_table[bucket_index] = new_item
        else:
            previous.next = new_item
        
        self.size += 1
        return True

    # Returns all the values within the HashTable (All items in buckets), Author: Diego Osorio
    def values(self):
        arr_of_values = []
        
        for bucket in self.patient_table:
            item = bucket

            while item is not None:
            # Iterates through the bucket and appends the value to the earlier array to be returned
                arr_of_values.append(item.value)
                item = item.next
        return arr_of_values
    
    # Deletion of a patient in the hash table by key, Author: Diego Osorio
    def pop(self, key):
        bucket_index = self.hashKey(key) % len(self.patient_table)
        item = self.patient_table[bucket_index]
        previous_item = None
        # Checks that the item is not None while searching the nodes of the buckets so as to not throw an error
        while item != None:
            # If key is found it runs a check on the first item and removes it if true
            if key == item.key:
                if previous_item == None:
                    self.patient_table[bucket_index] = item.next
                # Otherwise set the previous to the item's next thereby removing the node between
                else:
                    previous_item.next = item.next
                return True
            # Iterating through the bucket of keys
            previous_item = item
            item = item.next
        return False