# 第三周总结
## 递归
* 递归要点
终止条件；处理当前层；进入下一层；清除当前变量（可选）
* 递归代码模板    
```
Python   
def recursion(level, param1, param2, ...):    
    1 recursion terminator    
    if level > MAX_LEVEL:    
	   process_result    
	   return    
    2 process logic in current level    
    process(level, data...)    
    3 drill down    
    self.recursion(level + 1, p1, ...)    
    4 reverse the current level status if needed   
```

## 回溯  
* 回溯要点  
终止条件；选择、下一步、撤销选择；清除当前变量（可选）  
* 回溯代码模板  
```  
result = []     
def backtrack(路径, 选择列表):    
    if 满足结束条件:    
        result.add(路径)     
        return    
        
    for 选择 in 选择列表:      
        做选择      
        backtrack(路径, 选择列表)      
        撤销选择     
```

## 分治
* 分治要点     
终止条件；分解子问题、处理子问题、合并结果；清除当前变量（可选）      
* 分治代码模板      
```  
Python   
def divide_conquer(problem, param1, param2, ...):    
  1 recursion terminator    
  if problem is None:    
	print_result    
	return    
   
  2 prepare data    
  data = prepare_data(problem)    
  subproblems = split_problem(problem, data)    
    
  3 conquer subproblems    
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)    
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)    
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)    
  …   
   
  4 process and generate the final result    
  result = process_result(subresult1, subresult2, subresult3, …)   
	   
  revert the current level states   
``` 

## 个人理解
分治和回溯是递归的特殊表现形式，都存在终止条件判断，变化点在于如何处理当前层和进入下一层。
回溯先进行选择后进入下一层，最后撤回选择；分治是先分解子问题，再进入下一层，最后合并结果。
本质上并没有什么不同，只是处理当前层的方式有些不同。