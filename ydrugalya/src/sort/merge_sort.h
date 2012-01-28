#include "stdafx.h"

namespace al
{
	
	/** 
		основоной процедругой при сотрировке слиянием 
		явлется процедура merge
		процедура принимается на вход две отортированные
		последовательности и "мержит" их. 
		Здесь полезно представить себе 2 колоды карт 
		упорядоченные по старшинству. На каждом шаге 
		сравниваем 2 верхние карты из каждой стопки
		младшую - забираем. Сл. шагом поять сравниваем
		2 карты и т.д.
		@param a - исходные массив
		@param p - начало последовательности
		@param r - конец последовательности
		p <= q < r
	*/
	void merge(int A[], const int p, const int q, const int r)
	{
		const int n1 = q - p;	  // левая половина массив
		
		const int n2 = r - q; // правая половина массива
		
		int *L = new int[n1];
		
		int *R = new int[n2];

		
		for (int i = 0;  i < n1; ++i)
			L[i] = A[p + i];

		for (int i = 0; i < n2; ++i)
			R[i] = A[q + i]; 

		
		int i = 0;
		
		int j = 0;

		int k = 0;

		
		while(i < n1 || j < n2)
		{
			if (i < n1 && ( L[i] <= R[j] || j == n2))
			{
				A[p + k] = L[i];
				++i;
			}
			else if ( (j < n2) && (L[i] > R[j] || (i == n1) ))
			{
				A[p + k] = R[j];
				++j;
			}
			++k;
		}


		delete[] L; delete[] R;
	}


	void merge_sort(int A[], const int p, const int r)
	{
		if (r - p > 1 )
		{
			const int q =  (p + r) / 2;
			merge_sort(A, p, q); // сортируем левую половину массива 
			merge_sort(A, q, r); // сортируем правуб половину массива
			merge(A, p, q, r);   // соединем их
		}
	}
};// namespace al
