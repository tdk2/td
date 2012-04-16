#include "../dp/knapsack.h"

namespace al {

	void knapsack_demo() {
		using namespace dp;
		items_t items;
		const unsigned short KNAPSACK_WEIGHT = 5;
		items.push_back(  Item(3, 5) );
		items.push_back(  Item(2, 3) );
		items.push_back(  Item(1, 4) );

		solution_matrix_t c;
		knapsack_solve(items, KNAPSACK_WEIGHT, c);
		knapsack_reconstruct(c, items);
	}
}
