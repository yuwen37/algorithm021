#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存机制
#

# @lc code=start
class DLinkNode():
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetohead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = DLinkNode(key,value)
            self.addtohead(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                removed = self.removetail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            self.movetohead(node)
            node.value = value
    
    def addtohead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removenode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def removetail(self):
        node = self.tail.prev
        self.removenode(node)
        return node
        
    def movetohead(self, node):
        self.removenode(node)
        self.addtohead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

