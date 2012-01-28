#include <stdio.h>
#include <string.h>


namespace al {

const int q = 100001;

size_t hash(char* str, size_t m, size_t b, size_t bm) {
    size_t res = 0;
    for(size_t i = 0; i < m; ++i)  {
        res += (str[i] * bm) % q;
        bm /= b;
    }

    return res;
}


size_t rehash(char oldHead, char newHead, size_t oldHash, char newTail, size_t bm, size_t b) {
    size_t res = (oldHash - (bm * oldHead) ) % q;
    res =  (res * b) % q;
    res += newTail % q;
    return res;   
}

size_t find_substr(char* P, size_t m, char *T, size_t n) {
   
    size_t b = 2;
    size_t bM = b;

    // compute b ^ m - 1
    for(size_t i = 1; i < m - 1; ++i) {
         bM = (bM * b) % q;
    }

    size_t pHash = hash(P, m, b, bM);
    size_t tHash = hash(T, m, b, bM);
    
    for(size_t i = 0; i < n - m; ++i) {
        if ( pHash == tHash && (memcmp(P, &T[i], m) == 0) ) {
            return i;
        }

        tHash = rehash(T[i], T[i + 1], tHash, T[i + m] , bM, b);
        //tHash = hash(&T[i + 1], m, b, bM);
    }

    return -1;
}

}