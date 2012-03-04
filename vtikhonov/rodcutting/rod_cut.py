import sys
sys.path.append(sys.path[0] + '/../hash')
import utils

class RodCutting:

   # returns optimal cut and corresponding revenue
   # user code: cut, revenue = findOptimal(...)
   # note: prices is [0..n-1] array of prices of i+1 cuts
   @staticmethod
   def findOptimal(prices):
      # i belongs to [0..len(prices)-1]
      def findMaxRevenue(prices, i):
         return 0
      return ([], 0)

if __name__=="__main__":
    #testSingle()
    #testMultiple()
    cuts, maxRevenue = RodCutting.findOptimal([1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    print "optimal cuts: ", cuts, ", revenue: ", maxRevenue

