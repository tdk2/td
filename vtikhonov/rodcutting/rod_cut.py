import sys
sys.path.append(sys.path[0] + '/../hash')
import utils

class RodCutting:

   # returns optimal cut and corresponding revenue
   # user code: cut, revenue = findOptimal(...)
   # note: prices is [0..n-1] array of prices of i+1 cuts
   def findOptimal(self, prices, n = 0):
      if n == 0:
         n = len(prices)
      #return ([], self.revenueBottomUp(prices, len(prices)))
      return (self.revenueBottomUp(prices, n))

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

      r = [None if i != 0 else 0 for i in xrange(n+1)]     
      return revenueMemoizeAux(prices, n, r)

   # using bottom-up recursive algorithm
   # n belongs to [1..len(prices)]
   def revenueBottomUp(self, prices, n):
      r = [None if i != 0 else 0 for i in xrange(n+1)]
      s = [0 for i in xrange(n+1)]
      for i in xrange(1, n+1):
         rs = [(prices[j] + r[i-j-1], j+1) for j in xrange(i)]
         r[i], s[i] = max(rs, key = lambda pair: pair[0])

      revenue = r[n]
      cuts = []
      while n > 0:
         cuts.append(s[n])
         n -= s[n]
      return (cuts, revenue)


if __name__=="__main__":
    rc = RodCutting()
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    cuts, maxRevenue = rc.findOptimal(prices, 8)
    print "optimal cuts: ", cuts, ", revenue: ", maxRevenue

