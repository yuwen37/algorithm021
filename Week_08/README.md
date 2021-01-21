# 第八周学习笔记  
## 位运算
主要掌握一些位运算技巧。目前用的比较多的有以下几个：   
* ```x&-x``` 取最小位1
* ```x&(x-1)``` 打掉最小位1
* ```>>n``` 左移n位
* ```<<n``` 右移n位
## 布隆过滤器和LRU缓存
### 布隆过滤器  
布隆过滤器添加元素  
1. 将要添加的元素给k个哈希函数
2. 得到对应于位数组上的k个位置
3. 将这k个位置设为1   
布隆过滤器查询元素
1. 将要查询的元素给k个哈希函数
2. 得到对应于位数组上的k个位置
3. 如果k个位置有一个为0，则肯定不在集合中
4. 如果k个位置全部为1，则可能在集合中
特点
* 空间效率和查询效率高
* 有一定的误判率（哈希表是精确匹配）
### LRU缓存
```
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()
        self.remain = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        value = self.dic.pop(key)
        self.dic[key] = value
        return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value
```
## 排序算法
### 快速排序
```
def quick_sort(A,left,right):  # 这个本质思想就是确定中间一个值的位置,并把小于中间值的放到中间值前面，大于的放到后面
    if left < right:
        mid = partition(A,left,right)  
        quick_sort_c(A, left, mid-1) 
        quick_sort_c(A, mid+1, right)
    
def partition(A,left,right):  # 把小于pivot的值放前面，大于q的值放后面
    pivot = A[right]  # 确定中间值的位置，一般是第一个、中间一个和最后一个数字
    i = left
    for j in range(left,right):
        if A[j] < pivot:
            A[j],A[i] = A[i],A[j]
            i+=1
    A[right],A[i] = A[i],A[right]
    return i
```
### 归并排序
```
def merge(nums,left,mid,right):
    i, j = left, mid+1
    tmp=[]
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    if i > mid:
        tmp += nums[j:right+1]
    else:
        tmp += nums[i:mid+1]
    nums[left:right+1] = tmp

def merge_sort(nums,left,right):
    if left >= right:return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)
    merge(nums, left, mid, right)
```

