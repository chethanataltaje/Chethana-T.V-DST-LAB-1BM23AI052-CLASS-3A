# Enter your code here. Read input from STDIN. Print output to STDOUT
class TwoStackQueue:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, x):
        self.stack1.append(x) 

    def dequeue(self):
        if not self.stack2:  
            while self.stack1:
                self.stack2.append(self.stack1.pop()) 
        if self.stack2:  
            return self.stack2.pop()

    def front(self):
        if not self.stack2: 
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:  
            return self.stack2[-1] 


if __name__=="__main__":
    q=int(input())  
    queue=TwoStackQueue()  

    for _ in range(q):
        query=input().split()  
        task=int(query[0])  

        if task==1:
            queue.enqueue(int(query[1]))  
        elif task==2:
            queue.dequeue()  
        elif task==3:
            print(queue.front()) 
#Test case as per hackerrank
10
1 76
1 33
2
1 23
1 97
1 21
3
3
1 74
3
#output
33
33
33
