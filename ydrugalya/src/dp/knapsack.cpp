#include "knapsack.h"
#include <iostream>

namespace al { namespace dp {


void knapsack_solve(const items_t& items,  size_t knapsackSize, solution_matrix_t&/*out*/ c) {

	c.clear();

	// 1. Initialize solution matrix
	const size_t itemsCount = items.size();
	for(size_t i = 0; i < itemsCount + 1/*add extra row for convinience*/; ++i) {
		values_t values;
		values.resize(knapsackSize + 1 /*add extra column for conviniece*/);
		c.push_back(values);
	}

	// 2. Solution
	// c[i][w] - maximum value (v) we can maintain for i items with the weight <= w
	// i - i - current item index
	for(size_t i = 1; i <= itemsCount; ++i)
	{
		const Item& item = items[i - 1];
		for(value_t w = 1; w <= knapsackSize; ++w) {
			
			const size_t itemWieght = item.weigth();
			//const weight_t itemValue = item.value();

			value_t prevSizeOptimalSolution = c[i - 1][w];
			if (itemWieght > w)	{
				// to heavy baby! leave previous solution
				c[i][w] = prevSizeOptimalSolution;
			} else {
				// decide which one is better.  previous one for i-1 knapsack size - c[i - 1][w]
				// or it is better to get rid of previous solution and and check what if we add current item value to
				// 'pre-previous' c[i -1][w - wi] solution current value (vi)
				value_t prevPrevSizeOptimalSolution = c[i -1][w - itemWieght];
				c[i][w] = std::max( prevSizeOptimalSolution, prevPrevSizeOptimalSolution + item.value() );
			}
		}
	}
}

void knapsack_reconstruct_recursive(const solution_matrix_t& c, const items_t& items, size_t i, size_t w) {
	if (i == 0 || w == 0) {
		return;
	}

	value_t prevSizeOptimalSolution = c[i - 1][w];
	value_t currentValue = c[i][w];
	const Item& item = items[i - 1];
	// where optimal solution came from ? 
	if ( currentValue == prevSizeOptimalSolution) {
		knapsack_reconstruct_recursive(c, items, i - 1, w );
	} else {
		value_t prevPrevSizeOptimalSolution = c[i - 1][ w - item.weigth() ];
		std::cout << "Item " << item.weigth() << " " << item.value() << std::endl;
		knapsack_reconstruct_recursive(c, items, i - 1, w - item.weigth() );
	}
}

void knapsack_reconstruct(const solution_matrix_t& c, const items_t& items) {
	const size_t knapsackSize = items.size();
	const size_t itemsCount = items.size();
	knapsack_reconstruct_recursive(c, items, itemsCount, knapsackSize);
}

} } // namespace al { namespace dp {
