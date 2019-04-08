class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cQueue =[]
        self.queueSize =k
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): 
            return False 
        else: 
            self.cQueue.append(value)
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): 
            return False
        else: 
            self.cQueue.remove(self.Front())
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): 
            return -1 
        else: 
            return self.cQueue[0]

        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): 
            return -1 
        else: 
            return self.cQueue[len(self.cQueue)-1]
            

        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.cQueue) == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.cQueue) == self.queueSize
        
["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
[[3],[1],[2],[3],[4],[],[],[],[4],[]]


# # Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)
param_4 = obj.Rear()
param_4 = obj.isFull()
param_5 = obj.deQueue()
param_4 = obj.enQueue(4)
param_4 = obj.Rear()






# ["MyCircularQueue","enQueue","enQueue","Rear","isFull","enQueue","Rear","isEmpty","enQueue","enQueue","Rear","Front","Rear","enQueue","Front","deQueue","deQueue","deQueue","enQueue","deQueue","Rear","enQueue","enQueue","deQueue","Rear","deQueue","Front","enQueue","deQueue","Rear","enQueue","enQueue","enQueue","enQueue","Front","deQueue","enQueue","enQueue","enQueue","Rear","Rear","deQueue","Rear","enQueue","Front","Front","enQueue","isEmpty","enQueue","enQueue","Rear","Rear","Front","Front","isFull","Front","enQueue","Rear","enQueue","isEmpty","isEmpty","Front","Rear","Front","enQueue","isFull","enQueue","Rear","enQueue","Front","Rear","Rear","isFull","Rear","Front","Rear","Rear","Front","Front","enQueue","Front","enQueue","enQueue","enQueue","Rear","isFull","enQueue","enQueue","Front","deQueue","enQueue","isEmpty","deQueue","Front","Rear","Rear","deQueue","Front","deQueue","isEmpty","Rear","Front"]
# [[48],[60],[43],[],[],[10],[],[],[94],[52],[],[],[],[4],[],[],[],[],[60],[],[],[66],[61],[],[],[],[],[59],[],[],[24],[33],[4],[86],[],[],[51],[60],[16],[],[],[],[],[37],[],[],[10],[],[6],[28],[],[],[],[],[],[],[55],[],[42],[],[],[],[],[],[89],[],[81],[],[82],[],[],[],[],[],[],[],[],[],[],[19],[],[17],[74],[2],[],[],[59],[89],[],[],[72],[],[],[],[],[],[],[],[],[],[],[]]


# def buildFunctionString(funcName, param):

#     if len(param) > 0:
#         funcCall = "obj." + funcName + "(" + str(param[0]) + ")"
#     else:
#         funcCall = "obj." + funcName + "()"
    
#     return funcCall

# myList = ["MyCircularQueue","enQueue","enQueue","Rear","isFull","enQueue","Rear","isEmpty","enQueue","enQueue","Rear","Front","Rear","enQueue","Front","deQueue","deQueue","deQueue","enQueue","deQueue","Rear","enQueue","enQueue","deQueue","Rear","deQueue","Front","enQueue","deQueue","Rear","enQueue","enQueue","enQueue","enQueue","Front","deQueue","enQueue","enQueue","enQueue","Rear","Rear","deQueue","Rear","enQueue","Front","Front","enQueue","isEmpty","enQueue","enQueue","Rear","Rear","Front","Front","isFull","Front","enQueue","Rear","enQueue","isEmpty","isEmpty","Front","Rear","Front","enQueue","isFull","enQueue","Rear","enQueue","Front","Rear","Rear","isFull","Rear","Front","Rear","Rear","Front","Front","enQueue","Front","enQueue","enQueue","enQueue","Rear","isFull","enQueue","enQueue","Front","deQueue","enQueue","isEmpty","deQueue","Front","Rear","Rear","deQueue","Front","deQueue","isEmpty","Rear","Front"]
# myParams = [[48],[60],[43],[],[],[10],[],[],[94],[52],[],[],[],[4],[],[],[],[],[60],[],[],[66],[61],[],[],[],[],[59],[],[],[24],[33],[4],[86],[],[],[51],[60],[16],[],[],[],[],[37],[],[],[10],[],[6],[28],[],[],[],[],[],[],[55],[],[42],[],[],[],[],[],[89],[],[81],[],[82],[],[],[],[],[],[],[],[],[],[],[19],[],[17],[74],[2],[],[],[59],[89],[],[],[72],[],[],[],[],[],[],[],[],[],[],[]]

# for i in range(len(myList)):
#     print(buildFunctionString(myList[i], myParams[i]))

