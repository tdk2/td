#include "stdafx.h"
#include <algorithm>


namespace al
{
	/*
	* 1. Divide: Partition into 2 sub arrays around pivot
 	* such that elements in lower sub array <= x  element's 
	* and elements in upper sub array >= x
	* | x <= |x| > x |
	* 
	* 2. Conquer: recursively sort two sub arrays
	*
	* 3. Combine: trivial. everything is already sorted.
	*/
		
	// Ex. 
	// 6 10 13 5 8 3 2 11  x = 6
    // i  j 
    // scanning right and find 5. 
	// exchange it  with 10 (i+1)
	// 6 5 13 10 8 3 2 11  x = 6
	//   i       j
	// scanning right: 3 is less or equal then pivot
	// exchange  it it 13(i+1):
	// 6 5  3 10 8 13 2 11  x = 6
	//      i         j
	// scanning right: 2 is less or equal then pivot.
	// exchange it with 10 (i + 1)
	// 6 5  3 2 8 13 10 11  x = 6
	//        i         j
	// put pivot in the middle
	
	// 5 3 2 6 8 13 10 11  x = 6
	//   =< 6  | > 6        
		
	
	const int partition(int A[], const int p, const int q) // A[p..q]
	{
		int x = A[p]; // pivot A[p]

		int i = p;
		
		for (int j = p + 1; j < q; ++j)
		{
		   if (A[j] <= x)
		   {
			 ++i;
			 std::swap(A[i], A[j]);
		   }
		}

		std::swap( A[p] , A[i] );

		return i;
	}

	void quick_sort(int A[], const int p, const int q)
	{
        if (p >= q)
            return;
		
		const int r = partition(A, p, q);
		quick_sort(A, p, r);
		quick_sort(A, r + 1, q);
		
	}

};// namespace al


