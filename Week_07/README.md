# 第七周学习笔记
## Trie树(字典树)
字典树是以字典的形式存放，是一种树形结构，是一种哈希树的变种。  
典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。  
它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。  
三个基本性质：  
* 根节点不包含字符，除根节点外每一个节点都只包含一个字符；  
* 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串；  
* 每个节点的所有子节点包含的字符都不相同。
Python模板  
```
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '#'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root # 注意：这里下面虽然是对node进行改变，但是字典是可变类型，所以self.root也会跟着改变
        for char in word:
            node = node.setdefault(char, {}) # 如果含有char,则node进入char,也就是进入下一层。否则以char为键创建空字典
        node[self.end] = self.end
        # node[self.end] = node.get(self.end, 0) + 1 # 叶子节点可以计算频次

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char] # 不断进入下一个子节点
        return self.end in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```
## 并查集
并查集是一种树型的数据结构，用于处理一些不相交集合（disjoint sets）的合并及查询问题。  
并查集的初始化定义用数组有两种方式，一种```p = [i for i in range(size)] ```,另一种```p = [i for -1 in range(size)] ```
当然也可以用字典来定义，一种```p = {i:i for i in range(size)} ```,另一种```p = {i:-1 for i in range(size)} ```,当然，其中的-1也可以替换成None或者其他形式，只要能和下标区别开就行，下标一般是从0开始的正整数，也就是除了从0开始的正整数其他形式的符号数字都能替换-1.  
字典形式的优势是可以不从0开始初始化，可以从任意值初始化。而数组形式必须从0开始初始化，且连续，因为数组是以下标作为索引的，不连续的话无法正确索引到根节点。所以综合来看还是用字典形式的更加方便。
```
<!-- 第一种定义方式 -->
class UnionFind:
    def __init__(self,size):
    <!-- # 初始化目前一种方式,用p[i] == None标记根节点-->
        self.p = {i:None for i in range(size)} 
    
    def find(self,x):
        root = x       
        while self.p[root] != None:
            root = self.p[root]
        <!-- # 路径压缩 -->
        while self.p[x] != root:
            x, self.p[x] = self.p[x], root
        return root
    
    def merge(self,x,y):
        if not self.is_connected(x,y):
            self.p[self.find(x)] = self.find(y)
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

<!-- 第二种定义方式 -->
class UnionFind:
    def __init__(self,size):
    <!-- # 初始化的另一种方式,用p[i] == i标记根节点 -->
        self.p = {i:i for i in range(size)}  
    
    def find(self,x):
        root = x       
        while self.p[root] != root:
            root = self.p[root]
        # 路径压缩
        while self.p[x] != root:
            x, self.p[x] = self.p[x], root
        return root
    
    def merge(self,x,y):
        if not self.is_connected(x,y):
            self.p[self.find(x)] = self.find(y)
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
```
上面讲的两种方式，都是初始化的时候就事先准备好了size长度的字典(或数组)，其实还可以初始化空字典，然后需要的时候再加入，只要新添加一个add()函数即可，这种方式不需要提前知道当前集合的大小，可以随意调整，更加方便。模板如下：  
```
class UnionFind:
    def __init__(self,size):
    <!-- # 初始化的另一种方式,用p[i] == i标记根节点 -->
        self.p = {}  
    
    def find(self,x):
        root = x       
        while self.p[root] != root:
            root = self.p[root]
        # 路径压缩
        while self.p[x] != root:
            x, self.p[x] = self.p[x], root
        return root
    
    def merge(self,x,y):
        if not self.is_connected(x,y):
            self.p[self.find(x)] = self.find(y)
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def add(self,x):
        if x not in self.p:
            self.p[x] = x
```
## 剪枝
个人觉得剪枝是一项经验活，剪枝一般用在回溯、递归、DFS里面去掉多余不需要的计算。但是很难用什么话语总结，一般是先写好递归代码，然后再思考如何剪枝降低时间复杂度。
## 双向BFS
双向BFS和单向BFS大同小异，只是从两边同时开始往中间查找。
Python模板如下
```
def BFS(graph, start, end):
    visited = set()
	front = {start}
    back = {end}

	while front:
        front_next = {}
        for node in front:
            visited.add(node)
            process(node)
		    nodes = generate_related_nodes(node) 
            if nodes in back:
                return ...
            front_next.add(nodes)
        
        front = front_next
        if len(front) > len(back):
            front, back = back, front
    
 	# other processing work 	
    ...
```
## A* search(启发式搜索)
以后再学吧   

## AVL树
AVL树是最先发明的自平衡二叉查找树。在AVL树中任何节点的两个子树的高度最大差别为1，所以它也被称为高度平衡树。  
AVL树的删除、插入、查找和普通搜索二叉树没什么区别。唯一有区别的是当删除、插入之后，AVL树变得不平衡之后，如何通过旋转重新变得平衡。
旋转有四种操作，需要牢记：  
* 左左：上部右旋一次
* 右右：上部左旋一次
* 左右：下部左旋一次，上部右旋一次
* 右左：下部右旋一次，上部左旋一次   
同时如果旋转的过程中还有子树，子树也要跟着调整  
不足：结点需要额外的存储空间、且调整次数频繁，维护成本高

## 红黑树
近似平衡二叉树，能够确保任何结点的左右子树的高度差小于两倍。   
红黑树满足条件如下：
* 根结点是黑色
* 每个结点要么是红色要么是黑色
* 每个叶结点(null结点，空结点)是黑色
* 不能有相邻的两个红色结点
* 从任何一个结点到其叶子结点的所有路径都包含相同数目的黑色结点  

### 红黑树对比
* 如果读操作远大于写，那么选择AVL树(微博、数据库)；如果写操作和读操作五五开，那么选择红黑树(map,set)
* AVL树查找会比红黑树快，写入、删除操作会慢。
* AVL树需要的存储空间比红黑树大，因为需要记录heights和factors(平衡因子),红黑树只要1bit来存储红黑(01)信息。
