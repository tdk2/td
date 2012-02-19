#pragma once

#include <algorithm>
#include <vector>

namespace al {

typedef std::vector<char> chars_t;

typedef unsigned int uint;
typedef std::vector<unsigned int> cnt_row_t;
typedef std::vector< cnt_row_t  > counters_t;



void LCS_Length( const chars_t& X, const chars_t& Y,  counters_t& /*out*/ counters) {
    // allocate counters table
    const size_t rows = X.size();
    const size_t cols = Y.size();

    counters.reserve(rows + 1);
    for(size_t i = 0; i < rows + 1; ++i) {
        counters.push_back( cnt_row_t(cols + 1) );
    }


    for(size_t i = 1; i < rows + 1; ++i)
    {
        for(size_t j = 1; j < cols + 1; ++j) {
            if ( X[i - 1] == Y[j - 1] ) {
                counters[i][j] = counters[i - 1][j - 1] + 1;
            } else if ( counters[i-1][j] >= counters[i][j-1] ) {
                counters[i][j] = counters[i-1][j];
            } else {
                counters[i][j] = counters[i][j - 1];
            }
        }
    }
}

void Print_LCS(const chars_t& X, const chars_t& Y, const counters_t& counters, uint i, uint j) {
    if (0 == i || 0 == j) {
        return;
    } 

    if (X[i - 1] == Y[j - 1]) {
        Print_LCS(X, Y, counters, i - 1, j -1);
        std::cout << X[i - 1];
    } else if ( counters[i-1][j] >= counters[i][j-1] )  {
         Print_LCS(X, Y, counters, i - 1, j);
    } else {
        Print_LCS(X, Y, counters, i, j - 1);
    }
}



}