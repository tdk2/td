using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace StringMatch
{
    interface IRollingHasher
    {
        int Hash(string source, int length);
        int Hash(int previous, string source, int length, int iteration);
    }
}
