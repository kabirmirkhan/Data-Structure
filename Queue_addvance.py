class Queue:
    def __init__(self) -> None:
        self.queue = []

    # Add the element
    def enqueue(self,item):
        self.queue.append(item)
    
    # Remove the element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # function to print queue

    def display(self):
        print(self.queue)
        print(len(self.queue))

    # Return self size

    def size(self):
        return len(self.queue)
    

my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
print('Before removing')
my_queue.display()
print("After removing")
my_queue.dequeue()
my_queue.display()


