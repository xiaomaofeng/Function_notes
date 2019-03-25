#include<vector>

void dfs(int Data[], int& count)
{
	vector<int>A;
	vector<int>B;
//	int A[5];
//	int B[5];
	for (int i = 0; i < 10; i++)
	{
//		if (i = 9)
//			count++;
//		B[i] = Data[10 - i];
		if (B.size() = A.size())
		{
			B.push_back(Data[10 - i - 1]);
		}
		else if (B.size() > A.size())
		{
			B.push_back(Data[10 - i - 1]);
			dfs(int Data[], int& count);
			B.pop_back();
			A.push_back(Data[10 - i - 1])
		}

	}

}

int main()
{
	int count = 0;

}