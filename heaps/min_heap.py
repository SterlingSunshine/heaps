class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)



class MinHeap:

    def __init__(self):
        self.store = []


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(1) *same space is added to the list every time but the behind the scenes buffer might be using more memory than this
        """
        self.store.append(HeapNode(key, (value if value else key)))
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if len(self.store) < 1:
            return
        
        self.swap(0, len(self.store) - 1)
        ret_node = self.store.pop(len(self.store) - 1)
        self.heap_down(0)

        print(self.store)

        return ret_node.value


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        if len(self.store) < 1:
            return True

        return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        if index is not 0 and self.store[index].key < self.store[(index - ((index +1) %2)) // 2].key:
            self.swap(index, ((index - ((index +1) %2)) // 2))
            self.heap_up((index - ((index +1) %2)) // 2)

        return

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        if len(self.store) > (index * 2 + 1) and self.store[index].key > self.store[index * 2 + 1].key:
            self.swap(index, (index * 2 + 1))
            self.heap_down((index * 2 + 1))
            self.heap_down(index)
        elif len(self.store) > (index * 2 + 2) and self.store[index].key > self.store[index * 2 + 2].key:
            self.swap(index, (index * 2 + 2))
            self.heap_down((index * 2 + 2))
            self.heap_down(index)

        return

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
