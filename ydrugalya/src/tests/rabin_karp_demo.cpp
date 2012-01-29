#include "../search/substring.h"
#include <iostream>

namespace al {

void rabin_karp_demo() {
    char* p = "badaabracadabra";
    char* m = "aabracadabra";
    size_t s = find_substr( m, strlen(m), p, strlen(p) );
    std::cout << s;
}

}