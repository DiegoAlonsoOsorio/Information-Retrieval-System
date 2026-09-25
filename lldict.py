from dict_abstract import DictAbstract

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None 

class LLDict(DictAbstract):
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size 

    # Searching for a node corresponding to a key, Author: Diego Osorio
    def __contains__(self, key):
        # Check if the list is empty
        if self.head == None:
            return False
        curr_node = self.head
        # If not empty then iterate through the list checking ID's that match the key, then return true
        if curr_node != None:
            while (curr_node):
            # If found then simply return True
                if curr_node.key == key:
                    return True
                curr_node = curr_node.next
            # If not found then simply return False
            return False

    #retrieve information
#Author Grace and Karan 
    def __getitem__(self, key):
        #standard python dict behaviour raises a key error if not found 
        temp = self.head
        while temp is not None:
            if temp.key == key:
                return temp.value
            temp = temp.next 
            #key is fed to key error for more context when printing message
        raise KeyError(key)

#Author: Grace and Karan 
    def __setitem__(self, key, value):
        temp = self.head

        while temp is not None:
            if temp.key == key:
                temp.value = value
                return
            temp = temp.next

        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

#Author Karan Athwal
    def values(self):
        #builds list of values via appending to results then returns it 
        results = []
        current = self.head 
        while current is not None:
            results.append(current.value)
            current = current.next 
        return results 

    # Deletion of node by key, Author: Diego Osorio
    def pop(self, key):
        # A check of null for the list, if none return list is empty
        if self.head == None:
            raise KeyError(key)
        # Assigning variables to head and the successor node
        prev_node = self.head
        curr_node = self.head.next
        # If not null then traverse list looking for correct node to remove
        if prev_node != None:
            while(prev_node):
                # Check if the current node is the key to delete
                if prev_node.key == key:
                    # Assigning the head to the node being deleted's next node
                    self.head = prev_node.next
                    self.size -= 1
                    return prev_node.value
                # If node is not found then return
                if curr_node == None:
                    raise KeyError(key)
                if curr_node.key == key:
                    # Assign the previous node to the node being deleted's next node
                    prev_node.next = curr_node.next
                    self.size -= 1 
                    return curr_node.value
                # Continuing traversal of the nodes
                prev_node = curr_node
                curr_node = curr_node.next