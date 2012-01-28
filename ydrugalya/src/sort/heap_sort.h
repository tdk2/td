#include "stdafx.h"
#include <algorithm>


namespace al
{

const int parent(const int i)
{
	return i/2;
}

const int left(const int i)
{
	return 2*i + 1;
}

const int right(const int i)
{
	return 2*i + 2;
}

// эта процедруа служит дл€ поддержки свойсва 
// невозрастающей прирамиды
// max_heapify опускает значение элемента
// A[i] вниз по пирамиде, до тех пор
// пока он не станет на свое место, т.е. пока поддерево 
// с корнем наход€щимс€ в элементе i не станет невозрастающей
// пирамидой. дервео может бы и одноэелемнтным
// на кажом шаге производитс€ анализ, A[Lerft[i]], A[rigtjh[i]]
// A[i] индекс максимального элемента запоминаетс€, если максимальный
// элементи есть A[i] то делать особо нефиг, т.к. данное поддерево
// удовлетво€рет требованию невозрастающей пирамиды
void max_heapify(int A[], const int i, const int heap_size)
{
	const int l = left(i);
	const int r = right(i);
	// провер€ем удовл€твор€ет ли вставл€емый
	// элемент свойству невозрастаюзей пирамиды
	int largest = 0;

	if (l < heap_size && A[l] > A[i])
		largest = l;
	else
		largest = i;
	if (r <= heap_size && A[r] > largest)
		largest = r;

	if (largest != i)
	{
		std::swap(A[i], largest);
		max_heapify(A, largest, heap_size);
	}
}

// последовательным вызовом max_heapify можно 
// преобразовать массив в невозрастающую пирамиду
// причет можно можно это проделать только до узла 
// A[n/2] + 1 .. n
void build_max_heap(int A[], const int len)
{
	for (int i=len/2; i>=0; --i)
		max_heapify(A, i, len);
}

void heap_sort(int A[], const int len)
{
	build_max_heap(A, len);
	int heap_size = len;
	for (int i=len; i >=1; ++i)
	{
		std::swap(A[i], A[0]); 
		max_heapify(A, 1, --heap_size);
	}
}

};// namespace al


