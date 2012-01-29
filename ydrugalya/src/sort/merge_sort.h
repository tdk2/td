#include "stdafx.h"

namespace al
{
	
	/** 
		��������� ����������� ��� ���������� �������� 
		������� ��������� merge
		��������� ����������� �� ���� ��� ��������������
		������������������ � "������" ��. 
		����� ������� ����������� ���� 2 ������ ���� 
		������������� �� �����������. �� ������ ���� 
		���������� 2 ������� ����� �� ������ ������
		������� - ��������. ��. ����� ����� ����������
		2 ����� � �.�.
		@param a - �������� ������
		@param p - ������ ������������������
		@param r - ����� ������������������
		p <= q < r
	*/
	void merge(int A[], const int p, const int q, const int r)
	{
		const int n1 = q - p;	  // ����� �������� ������
		
		const int n2 = r - q; // ������ �������� �������
		
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
			merge_sort(A, p, q); // ��������� ����� �������� ������� 
			merge_sort(A, q, r); // ��������� ������ �������� �������
			merge(A, p, q, r);   // �������� ��
		}
	}
};// namespace al
