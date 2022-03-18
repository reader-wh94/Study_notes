class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, data):
    self.queue.append(data)
    
  def dequeue(self):
    dequeue_object = None
    if not self.isEmpty():
      dequeue_object = self.queue[0]
      self.queue = self.queue[1:]
      return dequeue_object
    else:
      print("Queue is empty")
      exit()
  
  def peek(self):
    if not self.isEmpty():
      return self.queue[0]
    else:
      print("Queue is empty")
      exit()
  
  def isEmpty(self):
    is_empty = False
    if len(self.queue) == 0:
      is_empty = True
    return is_empty
  
#test
q = Queue()
q.enqueue(5)
q.enqueue(7)
print(q.peek())
q.enqueue(8)
q.dequeue()
print(q.peek())