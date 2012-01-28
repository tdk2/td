#include "nth_element_demo.h"
#include "nth_element.h"

namespace al {
void nth_element_demo() {

    int A[] = {13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11, 13, 6, 8};
    int B[] = {13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11, 13, 6, 8};
    
    const size_t ARR_LEN = sizeof(A) / sizeof( A[0] );

    for(int i = 0; i < ARR_LEN; ++i) {
        int ithElement = Select<int>(A, 0, ARR_LEN, i);
        printf("Select %dth element is %d\n", i,  ithElement);

        ithElement = Select1<int>(B, 0, ARR_LEN, i);
        printf("Select1 %dth element is %d\n", i, ithElement);
    }
}

}
