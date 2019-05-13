#include<algorithm>
using namespace std;
template <typename ElementType>
int split(ElementType x[], int first, int last)
{
	ElementType pivot = x[first];
	int left = first;
	int right = last;
	while (left < right)
	{
		while (pivot < x[right])
			right--;
		while (left < right && (x[left] < pivot || x[left] == pivot))
			left++;
		if (left < right)
			swap(x[left], x[right]);

			
	}
	int pos = right;
	x[first] = x[pos];
	x[pos] = pivot;
	return pos;
}

template <typename ElementType>
void quicksort(ElementType x[], int first, int last)
{
	int pos;
	if (first < last)
	{
		pos = split(x, first, last)
		quicksort(x, first, pos - 1);
		quicksort(x, pos + 1, last); 
	}
}