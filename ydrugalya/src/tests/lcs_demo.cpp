#include <iostream>
#include "../search/lcs.h"

namespace al {

void strToVec(const std::string& str,  chars_t& vec/**/ )
{
    for(size_t i = 0; i < str.size(); ++i)
    {
        vec.push_back(str[i]);
    }

}
void lcs_demo() {
    
    counters_t counters;
    chars_t X;
    chars_t Y;

    strToVec("ABCBDAB", X);
    strToVec("BDCABA", Y);

    LCS_Length(X, Y, /*out*/ counters);


    for(size_t i = 0; i < X.size()  + 1; ++i)
    {
        for(size_t j = 0; j < Y.size()  + 1; ++j)
        {
            std::cout << counters[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    Print_LCS( X, Y, counters, X.size(), Y.size() );

}


}
