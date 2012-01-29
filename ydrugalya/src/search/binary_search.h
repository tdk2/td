#include "stdafx.h"


namespace al
{

// середину последовательности сравниваем
// с искомым элементом. если середина больше - 
// то продолжаем поиск в левой половине. меньше - 
// в правой
// анализ. как много раз массив длиной n может быть поделен пополам?
int binary_search_recursive(int a[], const int p, const int r,const int v)
{

	if (r - p == 1)
		return -1;

	const int h  = (r-p)/2 + p; 

	const int hv = a[h];

	if (hv == v)
		return h;
	else if (v > hv)
		return binary_search_recursive(a, h, r, v);
	else //  v < hv
		return binary_search_recursive(a, p, h, v);
}

// нерукурсивная версия того же алгортма
int binary_search(int a[], const int p, const int r, const int v)
{
	
	int pidx = p;
	int ridx = r;

	while (pidx != ridx)
	{
		const int h = (ridx-pidx)/2 + pidx;

		const int hv  =  a[h];

		if (hv == v)
			return h;
		else if (v > hv)
			pidx = h;
		else // v < hv
			ridx = h;
	}

	return -1;
}


#if 0

std::pair<int, int> find_pair(int A[], const int length, const int sum)
{
    al::merge_sort(A, 0, length); // n*lg(n)
    bool found = false;
    int i = 0;
    std::pair<int, int> res = std::make_pair(-1, -1);
    while (!found && i < length - 1)
    {
        if (A[i] < sum)
        {
            const int find_what = sum-A[i];

            const int idx_second 
                = al::binary_search_recursive(A, i+1, length, find_what);

            if (idx_second != -1)
            {
                res = std::make_pair(i, idx_second);
                break;
            }
        }
        ++i;
    }

    return res;
}

#endif

}; // namespace al