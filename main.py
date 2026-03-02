import numpy as np

class heap:
 
    def __init__ (self): #Initiation Function
        self.arr = []
        self.len = 0
    
    def peek(self): #Looks at top item of heap
        if self.len == 0:
            return "Error: Nothing to peek"
        else:
            return(self.arr[0])
    
    def pop(self): #Stores top item, copies bottom item onto top item, splits the last value off of the array, heapifies down, returns original top item
        if self.len == 1:
            root = self.arr[0]
            self.arr = []
            self.len -= 1
            return root
        if self.len == 0:
            return "Error: Heap Empty, cannot pop"
        root = self.arr[0]
        self.arr[0] = self.arr[self.len - 1]
        self.arr.pop(self.len - 1)
        self.len -= 1
        if self.len == 0: return root
        heap.heapifyDown(self)
        return root
    
    def insert(self, val): #inserts a new item in last index and then heapifies up
        self.arr.append(val)
        self.len += 1
        heap.heapifyUp(self, self.len - 1)
        
    def heapifyUp(self, index): #Checks if parent is greater than child, if true, swap parent and child, make new focus parent index
        if self.len == 1:
            return
        if self.len == 0:
            return "Error: Heap Empty, cannot heapify up"
        current = index
        parent = int(np.trunc((current-1)/2))
        cur = self.arr[current]
        par = self.arr[parent]
        while cur.dist < par.dist:
            self.arr[current] = par
            self.arr[parent] = cur
            current = parent
            parent = int(np.trunc((current-1)/2))
            if parent < 0: return
            cur = self.arr[current]
            par = self.arr[parent]
        return
 
    def heapifyDown(self): #checks if either child is less than parent, if true, swaps parent with the lowest child and then makes that child index the new focus
        current = 0
        
        if self.len == 1:
            return
        if self.len == 0:
            return "Error: Heap Empty, cannot heapify down"
        
        left = 2*current + 1
        right = 2*current + 2
        
        while True:
            left = 2*current + 1
            right = 2*current + 2
            smallest = current
            
            if left < self.len and self.arr[left].dist < self.arr[smallest].dist:
                smallest = left
            if right < self.len and self.arr[right].dist < self.arr[smallest].dist:
                smallest = right
            
            if smallest == current:  # heap property satisfied
                break
            
            # Swap parent with smallest child
            self.arr[current], self.arr[smallest] = self.arr[smallest], self.arr[current]
            current = smallest
 
    def printAll(self): #Prints each number in the array, goes down a row each time you print one more than the sum total of the previous rows
        for element in self.arr:
            print(element.name + " - " + str(element.adMap.items()))

    def decreaseKey(self, node, key):
        counter = 0
        for i in self.arr:
            if i.name == node:
                i.dist = key
                self.heapifyUp(counter)
            counter += 1

class node:
    
    def __init__ (self, name, adMap):
        self.name = name
        self.dist = float('inf')
        self.path = ""
        self.adMap = adMap
        
        

def main():
    nodeArr = []
    nodeDict = {}
    start = None
    end = None
    nodeName = ""
    index = 0
    dijkstraHeap = heap()
    fileName = input("Enter file name: ")
    
    with open(fileName, 'r') as file:
        nodeCounter = -2
        for line in file:
            tokens = []
            line = line.strip('\n')
            print(line)
            tokens = line.split(',')
            if nodeCounter == -2:
                nodeArr = tokens
                print(nodeArr)
            elif nodeCounter == -1:
                start = tokens[0]
                end = tokens[1]
            else:
                adjacencyMap = {}
                tokenIndex = 0
                for token in tokens:
                    if (token != "-"):
                        temp = {nodeArr[tokenIndex] : int(token)}
                        adjacencyMap.update(temp)
                    tokenIndex += 1
                newNode = node(nodeArr[nodeCounter], adjacencyMap)
                temp = {nodeArr[nodeCounter] : newNode}
                nodeDict.update(temp)
                dijkstraHeap.insert(newNode)
            nodeCounter += 1

    dijkstraHeap.printAll();
    
    dijkstraHeap.decreaseKey(start, 0)
    
    while dijkstraHeap.len > 0:
        currentNode = dijkstraHeap.peek()
        adIndex = 0
        for key, value in currentNode.adMap.items():
            nextDist = value
            nextNodeName = key
            nextNode = nodeDict[key]
            if nextNode.dist > currentNode.dist + nextDist:
                nextNode.dist = currentNode.dist + nextDist
                dijkstraHeap.decreaseKey(nextNode, nextNode.dist)
                nextNode.path = currentNode.path + "->" + nextNode.name
            adIndex += 1
        dijkstraHeap.pop()
    for value in nodeDict.values():
        print("Node Name: " + value.name + " Best Path: " + start + value.path + " Distance: " +  str(value.dist))
            
    

if __name__ == "__main__": #initializes main
    main()