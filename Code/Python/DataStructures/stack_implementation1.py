from collections import deque
from queue import LifoQueue

# stack = LifoQueue(maxsize = 3)

# print(stack.qsize())

# stack.put('a')
# stack.put('b')
# stack.put('c')

# print("Full: ", stack.full())
# print("Full: ", stack.qsize())

# print("Elements poped from stack")
# print(stack.get())
# print(stack.get())
# print(stack.get())

# print("Empty:",stack.empty())
# stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial Stack')
# print(stack)

# print('\nElements poped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\n Stack after elements are poped:')
# print(stack)

stack = []
stack.append('d')
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)
del stack[0]
stack.remove(stack[0])
stack.pop(0)
stack = stack[1:]
print(stack)

# print('Elements poped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('Stack after elements are poped:')
# print(stack)

