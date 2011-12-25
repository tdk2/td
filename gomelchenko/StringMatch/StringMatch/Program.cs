using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace StringMatch
{
    class Program
    {
        static void Main(string[] args)
        {
            var matcher = new RKStringMatcher(new RKHasher(RKStringMatcher.AlphabetLength));

            var results = matcher.FindSubstrings("baabaa", "aa");
            //results = matcher.FindSubstrings("lalabu", "bu");

            foreach (var shift in results)
            {
                Console.WriteLine(shift);
            }

            Console.ReadKey();
        }
    }
}
