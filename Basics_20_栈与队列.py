# 栈：先进后出

# 模拟栈结构
stack = []

# 压栈（向栈存数据）
stack.append("A")
print(stack)

stack.append("B")
print(stack)

stack.append("C")
print(stack)

# 出栈（在栈取数据）
res = stack.pop()
print(res)
print(stack)

res2 = stack.pop()
print(res2)
print(stack)

# 队列：先进先出
import collections

# 创建一个队列
queue = collections.deque()
print(queue)

# 进队（存数据）
queue.append("A")
print(queue)

queue.append("B")
print(queue)

queue.append("C")
print(queue)

# 出队（取数据）
res4 = queue.popleft()
print(res4)
print(queue)

res5 = queue.popleft()
print(res5)
print(queue)
