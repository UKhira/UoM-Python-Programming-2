my_queue = []

def enqueu(queue,value):
    queue.append(value)
    print(queue)

def dequeue(queue):
    return queue.pop(0)

enqueu(my_queue,'A')
enqueu(my_queue,'B')
enqueu(my_queue,'C')

print(dequeue(my_queue))
print(dequeue(my_queue))
print(dequeue(my_queue))

