// knapsack.cpp : Defines the entry point for the console application.
#include <vector>
#include <utility>

namespace al { namespace dp {

typedef unsigned int weight_t;
typedef unsigned int value_t;
typedef std::vector<value_t> values_t;
typedef std::vector< std::vector<value_t> > solution_matrix_t;

class Item : std::pair<weight_t, value_t> {
	typedef std::pair<weight_t, value_t> base_t;
public:
	Item(weight_t weigth, value_t val ) : base_t(weigth, val) { }
	weight_t weigth() const { return first; }
	value_t  value() const  { return second; }
};
typedef std::vector<Item> items_t;

void knapsack_solve(const items_t& items, size_t knapsackSize, solution_matrix_t&/*out*/ c);
void knapsack_reconstruct(const solution_matrix_t& c, const items_t& items);

} } // namespace al { namespace dp {
