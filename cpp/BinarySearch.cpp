int BinarySearch(List Tbl, ElementType K)
{
	/*Find keyword K in tabel Tbl*/
	int left, right, mid, NoFound = -1;
	left = 1;
	right = Tbl->Length;
	while (left <= right)
	{
		mid = (left + right) / 2;
		if (K < Tbl->Element[mid])
			right = mid - 1;//modify right boundary
		else if (K > Tbl->Element[mid])
			left = mid + 1;//modify left boundary
		else
			return mid;/*if found keyword, return index*/
	}
	return NotFound;/*if not found, return -1*/

}