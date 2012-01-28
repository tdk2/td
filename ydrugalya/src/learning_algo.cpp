#include "stdafx.h"

namespace al {
    void demo_hash_map();
    void bst_demo();
}

namespace al {
    void rabin_karp_demo();
    void radix_demo();
    void tree_demo();
}
int _tmain(int argc, _TCHAR* argv[])
{
    // al::radix_demo();   
    // al::nth_element_demo();
    // al::demo_hash_map();
    // al::rabin_karp_demo();
    al::radix_demo();
    al::bst_demo();
    return 0;
}

