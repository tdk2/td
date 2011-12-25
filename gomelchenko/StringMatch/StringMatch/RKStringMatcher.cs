using System;
using System.Collections.Generic;

namespace StringMatch
{
    class RKStringMatcher
    {
        // ASCII-printable symbols
        public const int AlphabetLength = 95;

        private IRollingHasher hasher;

        public RKStringMatcher(IRollingHasher hasher)
        {
            this.hasher = hasher;
        }
        
        public IEnumerable<int> FindSubstrings(string source, string pattern)
        {
            var result = new List<int>();

            var patternHash = hasher.Hash(pattern, pattern.Length);
            var sourceHash = hasher.Hash(source, pattern.Length);

            for (var i = 0; i <= source.Length - pattern.Length; i++ )
            {
                if ((patternHash == sourceHash) && IsEqual(source, pattern, i))
                {
                    result.Add(i);
                }

                if (i < source.Length - pattern.Length)
                {
                    sourceHash = hasher.Hash(sourceHash, source, pattern.Length, i);
                }
            }
            
            return result;
        }

        private static bool IsEqual(string source, string pattern, int begin)
        {
            for(var i = 0; i < pattern.Length; i++)
                if (source[begin + i] != pattern[i])
                    return false;
            return true;
        }

    }
}
