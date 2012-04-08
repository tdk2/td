#include <windows.h>
#include <tchar.h>

namespace al {
    void demo_hash_map();
    void bst_demo();
}

namespace al {
    void rabin_karp_demo();
    void radix_demo();
    void tree_demo();
    void rbt_demo();
    void lcs_demo();
	void knapsack_demo();
}
int _tmain(int argc, _TCHAR* argv[])
{
    // al::radix_demo();   
    // al::nth_element_demo();
    // al::demo_hash_map();
    // al::rabin_karp_demo();
    // al::radix_demo();
    // al::rbt_demo();
    // al::lcs_demo();
	al::knapsack_demo();
    return 0;
}

