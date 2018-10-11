import Queue

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = {} 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue) == 0 
  
    def insert(self, data, priority): 
        if self.queue.get(str(priority), None) == None:
            self.queue[str(priority)] = Queue.Queue()
        self.queue[str(priority)].put(data)
  
    def findMaxQueue(self):
        max = iter(self.queue.keys()).next()
        for x in self.queue:
            if int(x) < int(max):
                max = x
        return max

    def pop_element(self, max):
        item = self.queue[max].get()
        if self.queue[max].empty():
            del self.queue[max]
        return item

    def pop(self):
        try:
            max = self.findMaxQueue()
            return self.pop_element(max) 
        except IndexError: 
            print() 
            exit() 