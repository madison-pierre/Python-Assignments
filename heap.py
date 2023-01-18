# MADISON PIERRE
# heap.py
# 3/15/21
# This program contains implementation for a basic heap structure.
# We will expand on this for in class practice and for the homework
# A heap is a semi sorted datastructure that gives us instant access 
# to the item of most priority in the structure, typically the minimal
# or maximal value. This implementation is for min-heaps.

import random

class MinHeap:
	
    def __init__(self):
        self.size = 0
        self.data = [None]
    
    def peak(self):
        if self.size > 0:
            return self.data[1]
        else:
            return None
    
    def insert(self, item):
        if self.size == 0:
            self.data.append(item)
            self.size += 1
        else:
            self.heapify_up(item)
            self.size += 1
            
    def delete_min(self):
        if self.size > 0:
            result = self.peak()
            if self.size == 1:
                self.size=self.size-1
                return result
            self.data[1]=self.data.pop()
            self.size = self.size-1
            self.heapify_down(self.data[1])
        return result
            
            
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    def heapify_up(self, item):
        curr = self.size + 1
        self.data.append(item)
        print("*****************\nAt the start our data is this: %s" %self.data)
        while (curr > 1 and self.data[curr] < self.data[curr // 2]):
            print("Flipping %s and %s" % (self.data[curr], self.data[curr // 2]))
            self.swap(curr, curr // 2)
            print("The array is now: %s" % self.data)
            curr = curr // 2
    
    def heapify_down(self, item):
        curr = 1
        print("Current is: %s" % curr)
        print("Size is %s" % self.size)
        while(curr < self.size):
            if(curr*2 > self.size):
                break
            elif(curr*2+1 > self.size):
                if(self.data[curr] > self.data[curr*2]):
                    print("Swapping with left child")
                    self.swap(curr,curr*2)
                    curr=curr*2
                else:
                    break
            elif(self.data[curr*2] > self.data[curr*2 + 1]):
                if(self.data[curr] > self.data[curr*2 + 1]):
                    print("Swapping with right child")
                    self.swap(curr, curr*2 + 1)
                    curr = curr*2+1
                else:
                    break
            elif(self.data[curr*2] < self.data[curr*2 + 1]):
                if(self.data[curr] > self.data[curr*2]):
                    print("swapping with left child")
                    self.swap(curr, curr*2)
                    curr=curr*2
                else:
                    break
    
    def __str__(self):
        # return "%s" % self.data
        result = ""
        count = 2
        for i in range(1, len(self.data)):
            if i == count:
                count *= 2
                result += "\n"
            result += "%s\t" % self.data[i]
        return result
    
    def decrementAll(self,givenPeak):
        for item in range(1,self.size):
            item = item-givenPeak
        
    def checkoutSimulator(self,checkouts,checkoutTimes):
        counter=0
        while checkouts > 0:
            self.insert(checkoutTimes[counter])
            checkouts = checkouts-1
            counter=counter+1
        print("The heap we've built looks like: %s" % self)
        #Our heap is now built. We can now focus on breaking it down
        while self.size > 0:
            print("It's time to delete the min")
            peak=self.delete_min()
            print("Here's the min we deleted: %s" % peak)
            print("It's time to decrement")
            self.decrementAll(peak)
            print(self)
            print("Array is at size: %s" % self.size)


def main():
    print("Welcome to the heap code!")
    my_heap = MinHeap()
    
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(12)
    my_heap.insert(4)
    my_heap.insert(7)
    my_heap.insert(6)
    my_heap.insert(14)
    my_heap.insert(1)
    print(my_heap)

    print("We will now test delete min on the heap. It should delete 1.")
    my_heap.delete_min()
    print("After deletion the heap is ")
    print(my_heap)

    print("We will now test the grocery store simulation")
    new_heap=MinHeap()
    checkoutLocations = 7
    checkoutTimes = [3,7,3,4,5,10,9]
    print("Here is the new heap we made: %s" % new_heap)
    print("Here are all the checkout times: %s" % checkoutTimes)
    new_heap.checkoutSimulator(checkoutLocations,checkoutTimes)
    
    #my_heap2 = MinHeap()
    #print("\nLet us now add random numbers to our min heap and verify the performance")
    #to_add = []
    #for i in range(31):
        #to_add.append(random.randint(0,100))
        
    #print(to_add)
    #print("Now that we have generated a random array of ints, let us add themn to the min-heap")
        
    #for item in to_add:
        #my_heap2.insert(item)
        
    #print(my_heap2)


main()
