# 第四周总结
## 1.深度优先遍历与广度优先遍历     
广度优先更多的是利用双端队列来实现，深度优先更多的是利用递归来实现，也可以利用栈来实现。
```
#Python递归写法
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```
```
#Python非递归写法
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...

```
```
# Python 
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```
## 2.贪心算法  
贪心方法就是每次通过局部最优来获得全局最优，思想很简单，但是往往证明寻找局部最优能找到全局最优比较困难。

## 3.二分查找   
直接给出二分查找的三种模板
```   
# Python模板一
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = left + (right - left) // 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
```
# Python模板二
left, right = 0, len(array) - 1 
while left < right: 
	  mid = left + (right - left) // 2
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid
return left
```
```
# Python模板三
left, right = 0, len(array) - 1 
while left < right: 
	  mid = left + (right - left + 1) // 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid 
	  else: 
		    right = mid - 1
return left
```
从以上三种模板，可以看出一点套路， ``` mid = left + (right - left) // 2 ``` 与 ```left = mid + 1, right = mid``` 搭配； ``` mid = left + (right - left + 1) // 2 ``` 应该与 ```left = mid, right = mid - 1``` 搭配。而 ```left = mid + 1, right = mid - 1``` 容易使得 right < left ，所以不便与 ```while (left < right)``` 搭配。
其次```while left <= right```这种形式，结束后right < left，由于```mid = left + (right - left) // 2```使得mid是偏向left的，但是```right = mid - 1```其实并不太好，这里面会有重复部分，容易死循环。