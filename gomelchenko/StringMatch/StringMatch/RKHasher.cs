using System;
using System.Collections.Generic;

namespace StringMatch
{
    public class RKHasher : IRollingHasher
    {
        private readonly int _alphabetLength;
        private readonly int _modulus;

        public RKHasher(int alphabetLength, int modulus)
        {
            this._alphabetLength = alphabetLength;
            this._modulus = HashHelpers.IsPrime(modulus) ? modulus : GetDefaultModulus(alphabetLength);
        }

        public RKHasher(int alphabetLength)
            : this(alphabetLength, GetDefaultModulus(alphabetLength))
        {
        }

        public int Hash(string source, int length)
        {
            int hash = 0;
            for (var i = 0; i < length; i++)
            {
                hash = ((_alphabetLength) * hash + source[i]) % _modulus;
            }

            return hash;
        }

        public int Hash(int previous, string source, int length, int iteration)
        {
            int highestDigitModulo = (int)Math.Pow(_alphabetLength, length - 1) % _modulus;

            return (_alphabetLength * (previous - source[iteration] * highestDigitModulo) + source[iteration + length]) % _modulus;
        }

        private static int GetDefaultModulus(int alphabetLength)
        {
            return HashHelpers.GetMaxPrime(int.MaxValue / alphabetLength);
        }
    }
}