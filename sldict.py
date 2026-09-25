from dict_abstract import DictAbstract
import patient

class SLDict(DictAbstract):
    def __init__(self):
        self.sorted_list = []
        self.size = 0

    # Karan Athwal
    def __len__(self):
        return len(self.sorted_list)
 #added this so I could use my display function smoothly without a rewrite
    def __iter__(self):
        for key, value in self.sorted_list:
            yield key 

    # Karan Athwal
    def __contains__(self, key):
        for _key, value in self.sorted_list:
            if _key == key:
                return True 
        return False 
        
    
    #Grace Lasiter    
    def __getitem__(self, key):
        left = 0
        right = len(self.sorted_list) - 1

        while left <= right:
            middle = (left + right) // 2

            if self.sorted_list[middle][0] == key:
                return self.sorted_list[middle][1]
            elif key < self.sorted_list[middle][0]:
                right = middle - 1
            else:
                left = middle + 1

        raise KeyError(key)
    
    #Grace Lasiter
    def __setitem__(self, key, value):
        for i in range(len(self.sorted_list)):
            if self.sorted_list[i][0] == key:
                self.sorted_list[i] = (key, value)
                return

            if key < self.sorted_list[i][0]:
                self.sorted_list.insert(i, (key, value))
                self.size += 1
                return

        self.sorted_list.append((key, value))
        self.size += 1       
    
    # Author: Diego Osorio
    def values(self):
        list_of_values = []
        for key, value in self.sorted_list:
            list_of_values.append(value)
        return list_of_values

    # Author: Diego Osorio
    def pop(self, key):
        # Iterating through the list to find the patient to delete
        for i in range(0, len(self.sorted_list)):
            if self.sorted_list[i][0] == key:
                del self.sorted_list[i]
                self.size -= 1
                return True
        return False

    # Author: Diego Osorio
    #Binary Search was used because it is one of the most efficent methods of searching 
    #a list as it halves the number of elements to search
    def binary_search(self, key):
        middle = self.size // 2
        # Checks if the middle key is the right one
        if self.sorted_list[middle][0] == key:
            return self.sorted_list[middle][0]
        # Checks the right side of the list
        elif self.sorted_list[middle][0] < key:
            for i in range(middle, self.size):
                if self.sorted_list[i][0] == key:
                    return self.sorted_list[i][0]
                else:
                    raise KeyError(key)
        # Checks the left side of the list
        else:
            for i in range(0, middle):
                if self.sorted_list[i][0] == key:
                    return self.sorted_list[i][0]
                else:
                    raise KeyError(key)

    
    #author Karan Athwal 
    #quicksort was chosen because it is both easy to implement and very efficient when it comes to arrays
    #it also sorts in place with keeps space complexity O(1) 
    def _quick_sort(self):
       _sort(self.sorted_list, 0, len(self.sorted_list) - 1) 
    
    @staticmethod
    def _sort(arr, left, right):
        if left >= right:
            return 
        part = _partition(arr, left, right)
        _sort(arr, left, part - 1) 
        _sort(arr, part + 1, right)


    @staticmethod
    def _partition(arr, left, right):
        part = arr[right]._patient_id
        a =left - 1
        for i in range(left, right):
            if arr[i]._patient_id < part:
                a += 1 
                _swap(arr, a, i)
        a+= 1 
        _swap(arr, a, right)
        return a 

    @staticmethod
    def _swap(arr, a, b):
        temp = arr[b]
        arr[b] = arr[a] 
        arr[a] = temp 
