class PriorityQueue(object): 
    def __init__(self): 
        self.queue = {} 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue) == 0 
  
    def insert(self, data, priority): 
        self.queue[str(priority)] = [data]
  
    def pop(self): 
        try:
            max = -1
            for x in self.queue:
                if(max == -1):
                    max = x
                    continue
                if int(x) < int(max): 
                    max = x
            item = self.queue[max].pop()
            if len(self.queue[max]) == 0:
                del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 