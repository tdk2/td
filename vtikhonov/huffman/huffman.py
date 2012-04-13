""" 
Constructing huffman codes using greedy algorithms
"""

import sys
import heapq

class TreeNode:
   def __init__(self, value, frequency, left = None, right = None):
      self.Value = value
      self.Frequency = frequency
      self.Left = left
      self.Right = right
      
   def __lt__(	self, other):
      return self.Frequency < other.Frequency

   @staticmethod
   def merge(a, b):
      return TreeNode(None, a.Frequency + b.Frequency, a, b)

   def printCodesAndCost(self):
      bits = self.__printRecursiveLeaves('')
      print "\nthe tree cost is %d" % bits

   def __printRecursiveLeaves(self, prefix):
      bits = 0
      if self.Left != None:
         bits += self.Left.__printRecursiveLeaves(prefix + '0')
      if self.Value == None:
         #based on 16.3-3, the tree cost can be calculated over internal nodes as sum of frequences of children nodes
         bits += self.Frequency
      if (self.Left == None and self.Right == None and self.Value != None):
         print "('%c':%d:%s)" % (self.Value, self.Frequency, prefix),
      if self.Right != None:
         bits += self.Right.__printRecursiveLeaves(prefix + '1')
      return bits


def constructHuffman(buffer):
   length = len(buffer)
   if length < 2:
      print "Too short input buffer"
      return

   print "The buffer size is %d bits" % (8*len(buffer))

   bytes = {}
   for item in buffer:
      if item not in bytes:
         bytes[item] = 1
      else:
         bytes[item] = bytes[item]+1

   print "The buffer contains %d distinct bytes" % len(bytes.items())
   heap = map(lambda item: TreeNode(item[0], item[1]), bytes.items())
   heapq.heapify(heap)
   for i in xrange(len(bytes)-1):
      a, b = heapq.heappop(heap), heapq.heappop(heap)
      heapq.heappush(heap, TreeNode.merge(a, b))
   heap[0].printCodesAndCost()

   

if __name__=="__main__":
   fileName = sys.argv[0]
   if len(sys.argv) > 1:
      fileName = sys.argv[1]
   with open(fileName, 'rb') as f:
      constructHuffman(f.read())  


