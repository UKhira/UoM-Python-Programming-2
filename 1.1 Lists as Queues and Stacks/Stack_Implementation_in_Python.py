def push(stack,value):
    stack.append(value)
    print(stack)

def pop(stack):
    return stack.pop()                  #pop() method removes the last element in a list

my_stack = []
push(my_stack, 'a')                     #stack = my_stack,  value = 'a'  (arguments passed into parameters of push function)
push(my_stack, 'b')
push(my_stack, 'c')                     # stack[0] = 'a', stack[1] = 'b', stack[2] = 'c'. stack = ['a','b','c']

print(pop(my_stack))
print(pop(my_stack))
print(pop(my_stack))


