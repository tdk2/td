""" 
0-1 knapsack problem solution using dynamic programming.
"""

def solveKnapsack(W, items):
   # m is matrix m[i, w] is maximum value that can be attained with weight <= w
   # using items up to i, see http://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
   m = [[0 for w in xrange(W+1)] for i in xrange(len(items) + 1)]
   for i in xrange(1, len(m)):
      for w in xrange(1, W+1):
         v_i = items[i-1][0]
         w_i = items[i-1][1]
         if w_i > w:
            m[i][w] = m[i-1][w]
         else:
            m[i][w] = max(m[i-1][w], m[i-1][w-w_i] + v_i)

   # the bottom right element of the matrix is the best value for knapsack
   bestValue = m[len(items)][W]

   # reconstruct the list of items to pack the knapsack optimally
   bestItems = []
   itemIndex = len(items)
   remainedVolume = W
   while itemIndex > 0 and remainedVolume > 0:
      #detect if current item is contained in the best item set
      if m[itemIndex][remainedVolume] > m[itemIndex-1][remainedVolume]:
         bestItems.insert(0, items[itemIndex-1])
         remainedVolume -= items[itemIndex-1][1]
      itemIndex = itemIndex-1
   return (bestValue, bestItems)


if __name__=="__main__":
   print solveKnapsack(50, [(60, 10), (100, 20), (120, 30)])

