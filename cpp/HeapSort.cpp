#include<iostream>
#include<vector>
using namespace std;

class HeapSort
{
	//get the parent node index
	int parent(int i)
	{
		return(i - 1) / 2;
	}
	
	//get the left child node index
	int left(int i)
	{
		return 2 * i + 1;
	}

	//get the right child node index
	int right(int i)
	{
		return 2 * i + 2;
	}

	//build max heap
	void build_max_heapify(vector<int>&nums, int heap_size)
	{
		for (int i = heap_size / 2; i >= 0; --i)
		{
			max_heapify(nums, i, heap_size);
		}
		print_heap(nums, heap_size);
	}

	//build min heap
	void build_min_heapify(vector<int>&nums, int heap_size)
	{
		for (int i = heap_size / 2; i >= 0; --i)
		{
			min_heapify(nums, i, heap_size);
		}
		print_heap(nums, heap_size);
	}

	//adjust the heap to max-heap
	void max_heapify(vector<int>&nums, int k, int len)
	{
		while (k < len)
		{
			int max_index = k;
			//left leaf node search
			int l = left(k);
			if (l<len&&nums[l]>nums[max_index])
			{
				max_index = l;
			}

			//right leaf node search
			int r = right(k);
			if (r<len&&nums[r]>nums[max_index])
			{
				max_index = r;
			}

			//node after k are max_heap already
			if (k == max_index)
			{
				break;
			}

			//keep the root node the largest
			int temp = nums[k];
			nums[k] = nums[max_index];
			nums[max_index] = temp;
			//adjust not only just current index
			k = max_index;
		}
	}

	void min_heapify(vector<int>&nums, int k, int len)
	{
		while (k < len)
		{
			int min_index = k;
			//left leaf node search
			int l = left(k);
			if (l < len&&nums[l] < nums[min_index])
			{
				min_index = l;
			}

			//right leaf node search
			int r = right(k);
			if (r < len&&nums[r] < nums[min_index])
			{
				min_index = r;
			}

			//node after k are min_heap already
			if (k == min_index)
			{
				break;
			}

			//keep the root node the largest
			int temp = nums[k];
			nums[k] = nums[min_index];
			nums[min_index] = temp;
			//adjust not only just current index
			k = min_index;
		}
	}

	public:
		//heap sort
		void heap_sort(vector<int>&nums)
		{
			int len = nums.size();
			//init heap structure
			build_max_heapify(nums, len);
			//heap sort
			for (int i = len - 1; i >= 0; --i)
			{
				//put the largest number int the last
				int temp = nums[0];
				nums[0] = nums[i];
				nums[i] = temp;
				//reconstruct heap
				build_max_heapify(nums, i);
			}
			print_heap(nums, len);
		}

		//print heap between[0,heap_size-1]
		void print_heap(vector<int>&nums, int heap_size)
		{
			for (int i = 0; i < heap_size; ++i)
			{
				cout << nums[i] << ",";
			}
			cout << endl;
		}

		
};

//int main(int argc, char *argv[])
//{
//	int A[] = { 19,1,10,14,16,4,7,9,3,2,8,5,11 };
//	vector<int>nums;
//	for (int i = 0; i < sizeof(A) / sizeof(A[0]); ++i)
//	{
//		nums.push_back(A[i]);
//	}
//
//	HeapSort sort;
//	sort.print_heap(nums, nums.size());
//	sort.heap_sort(nums);
//	getchar();
//	return 0;
//}