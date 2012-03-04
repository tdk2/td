import sys
sys.path.append(sys.path[0] + '/../hash')
import utils

class RodCutting:

   # returns optimal cut and corresponding revenue
   # user code: cut, revenue = findOptimal(...)
   # note: prices is [0..n-1] array of prices of i+1 cuts
   def findOptimal(self, prices):
      return ([], self.revenueBottomUp(prices, len(prices)))

   # naive recursive implementation
   # n belongs to [1..len(prices)]
   def revenueNaive(self, prices, n):
      if n == 0:
         return 0
      else:
         return max([prices[i] + self.revenueNaive(prices, n-i-1) for i in xrange(n)])

   # using top-down recursive algorithm with memoization
   # n belongs to [1..len(prices)]
   def revenueMemoize(self, prices, n):
      # revenues [0..n]
      def revenueMemoizeAux(prices, n, revenues):
         if revenues[n] == None:
            # memoize it
            revenues[n] = max([prices[i] + revenueMemoizeAux(prices, n-i-1, revenues) for i in xrange(n)])
         return revenues[n]

      r = [None if i != 0 else 0 for i in xrange(0, n+1)]     
      return revenueMemoizeAux(prices, n, r)

   # using bottom-up recursive algorithm
   # n belongs to [1..len(prices)]
   def revenueBottomUp(self, prices, n):
      r = [None if i != 0 else 0 for i in xrange(0, n+1)]
      for i in xrange(1, n+1):
         r[i] = max([prices[j] + r[i-j-1] for j in xrange(i)])
      return r[n]


def generatePrices(n):
   return [2*(i+1) for i in xrange(n)]

if __name__=="__main__":
    #testSingle()
    #testMultiple()
    prices = generatePrices(1000)
    rc = RodCutting()
    #prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    cuts, maxRevenue = rc.findOptimal(prices)
    print "optimal cuts: ", cuts, ", revenue: ", maxRevenue

